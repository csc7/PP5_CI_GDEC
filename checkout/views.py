###############################################################################

"""
Django views for the checkout app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST
import stripe
import json

# INTERNAL:
from bag.contexts import bag_contents
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile

###############################################################################


# To check if the user has the "save info" box checked during payment
@require_POST
def cache_checkout_data(request):
    """
    View for the purchasing bag
    This function check if the user has the "save info" box checked
    during payment

    Parameters In: HTTP request object

    Parameters Out: HttpResponse onbject (200 or 500)
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    View for the checkout page

    Parameters In: HTTP request object

    Parameters Out: request, template (checkout/checkout.html),
    context variables:
        'order_form',
        'stripe_public_key',
        'client_secret'
    """

    # Read Stripe keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        # Check if form is valid, process it, and inform user
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            # Avoid multiple savings with commit=False
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]

            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()

            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    # if integer, then the item does not have resolution
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    # else, the item does have resolution
                    else:
                        for (resolution, quantity) in (
                                item_data['items_by_resolution'].items()):
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_resolution=resolution,
                            )
                            order_line_item.save()

                except Product.DoesNotExist:
                    messages.error(
                        request,
                        "One of the products in your bag wasn't"
                        "found in our database. "
                        "Please call us for assistance!")
                    order.delete()
                    return redirect(reverse('view_bag'))

            # Save info to user profile if all right
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number])
            )

        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(
                request,
                "There's nothing in your bag at the moment"
            )
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Load user data in the form if authenticated
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Missing Stripe public key. \
            Check if it is set in your environment.')

    # Variables to return
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    View for a success checkout

    Parameters In: HTTP request object, order number

    Parameters Out: request, template (checkout/checkout_success.html),
    context variables:
        'order'
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    # Save purshcase if user is authenticated
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)

        # Add user profile to order
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                    'default_phone_number': order.phone_number,
                    'default_country': order.country,
                    'default_postcode': order.postcode,
                    'default_town_or_city': order.town_or_city,
                    'default_street_address1': order.street_address1,
                    'default_street_address2': order.street_address2,
                    'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    # Inform user of the success order
    messages.success(request, f'Order successfully processed!\
        Order number: {order_number}\
        A confirmation e-mail is being sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    # Variables to return
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
