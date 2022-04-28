###############################################################################

"""
Django views for the wish list app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib import messages
import json

# INTERNAL:
from products.models import Product
from checkout.models import OrderLineItem
from profiles.models import UserProfile
from wish.models import WishList
from bag.templatetags.bag_tools import calc_subtotal

###############################################################################


# Wish list view
def view_wish_list(request):
    """View for the wish list

    Parameters In: HTTP request object

    Parameters Out: request object, template (wish/wish_list.html) and
    context variables:
        'products_in_wish_orders',
        'products_to_label_in_wish_list'
    """

    profile = get_object_or_404(UserProfile, user=request.user)
    wish_list_items = WishList.objects.filter(user_profile=profile)

    user_orders = profile.orders.all()
    products_in_wish_orders = OrderLineItem.objects.all()
    products_to_label_in_wish_list = \
        products_in_wish_orders.values_list('product_id', flat=True)

    context = {
        'products_in_wish_orders': wish_list_items.order_by('-id'),
        'products_to_label_in_wish_list': products_to_label_in_wish_list,
    }

    return render(request, 'wish/wish_list.html', context)


# View for adding products to the wish list
def add_to_wish_list(request, item_id):
    """ Add items to the wish list

    Parameters In: HTTP request object, product ID

    Parameters Out: redirect URL to wish list

    """

    resolution = None

    # Just check that AJAX post does not add "\n" at the end (last character)
    # is an "n", remember AJAX post inclue quotes ("") so first and last
    # characters need to be removed ([1:1] below)
    if (json.dumps(request.POST.get('resolution'))[-2].lower() == 'n'):
        resolution = json.dumps(request.POST.get('resolution'))[1:-3].lower()
    else:
        resolution = json.dumps(request.POST.get('resolution'))[1:-1].lower()
    ajax_id = json.dumps(request.POST.get('itemId'))[1:-1]
    item_id = ajax_id

    redirect_url = json.dumps(request.POST.get('redirect_url'))[1:-1]
    quantity = int(json.dumps(request.POST.get('quantity'))[1:-1])

    # Read product being added
    product = get_object_or_404(Product, pk=item_id)

    # Read user profile
    profile = get_object_or_404(UserProfile, user=request.user)

    # Read quantity, URL to redirect and compute line_item_total
    line_item_total = calc_subtotal(product.price, quantity)
    items_in_wish_list = WishList.objects.filter(user_profile=profile)

    if (resolution.lower() == 'high' or
            resolution.lower() == 'medium' or
            resolution.lower() == 'low'):

        try:
            update_wish_item = WishList.objects.get(
                user_profile=profile,
                product=product,
                product_resolution=resolution
            )

        except:
            new_wish_item = WishList.objects.create(
                user_profile=profile,
                product=product,
                product_resolution=resolution,
                quantity=quantity,
                lineitem_total=line_item_total
            )
            new_wish_item.save()
            messages.success(request, 'Product added to the wish list')

        else:
            update_wish_item.quantity = quantity
            update_wish_item.save()
            messages.success(request, 'Quantity updated in wish list')

    else:

        try:
            update_wish_item = WishList.objects.get(
                user_profile=profile,
                product=product,
            )

        except:
            new_wish_item = WishList.objects.create(
                user_profile=profile,
                product=product,
                quantity=quantity,
                lineitem_total=line_item_total
            )
            new_wish_item.save()
            messages.success(request, 'Product added to the wish list')

        else:
            update_wish_item.quantity = quantity
            update_wish_item.save()
            messages.success(request, 'Quantity updated in wish list')

    return HttpResponse(status=200)


# View for updating the wish list
def adjust_wish_list(request):
    """Adjust the quantity of items in the wish list

    Parameters In: HTTP request object

    Parameters Out: HttpResponse (200 or 500)

    """

    # Just check that AJAX post does not add "\n" at the end (last character)
    # is an "n", remember AJAX post inclue quotes ("") so first and last
    # characters need to be removed ([1:1] below)
    if (json.dumps(request.POST.get('resolution'))[-2].lower() == 'n'):
        resolution = json.dumps(request.POST.get('resolution'))[1:-3].lower()
    else:
        resolution = json.dumps(request.POST.get('resolution'))[1:-1].lower()
    ajax_id = json.dumps(request.POST.get('itemId'))[1:-1]
    quantity = json.dumps(request.POST.get('quantity'))[1:-1]

    # Read wish list content
    profile = get_object_or_404(UserProfile, user=request.user)

    # If product has resolution, read and compute it
    if (resolution == 'low' or resolution == 'medium' or
            resolution == 'high'):

        # Get record and update
        wish_item_to_update = WishList.objects.get(
            user_profile=profile,
            product=ajax_id,
            product_resolution=resolution
        )
        # Update record
        wish_item_to_update.quantity = quantity
        wish_item_to_update.save()
        messages.success(request, 'Product updated in wish list')

    else:
        wish_item_to_update = WishList.objects.get(
            user_profile=profile,
            product=ajax_id
        )

        # Update record
        wish_item_to_update.quantity = quantity
        wish_item_to_update.save()
        messages.success(request, 'Product updated in wish list')

    return HttpResponse(status=200)


def remove_from_wish_list(request):
    """Remove items from the wish_list

    Parameters In: HTTP request object

    Parameters Out: HttpResponse (200 or 500)

    """
    # Just check that AJAX post does not add "\n" at the end (last character)
    # is an "n", remember AJAX post inclue quotes ("") so first and last
    # characters need to be removed ([1:1] below)
    if (json.dumps(request.POST.get('resolution'))[-2].lower() == 'n'):
        resolution = json.dumps(request.POST.get('resolution'))[1:-3].lower()
    else:
        resolution = json.dumps(request.POST.get('resolution'))[1:-1].lower()
    ajax_id = json.dumps(request.POST.get('itemId'))[1:-1]

    # Try to delete product with resolution, if not possible it means
    # the product does not have it
    try:
        # Read wish list content
        profile = get_object_or_404(UserProfile, user=request.user)

        # Delete record
        if (resolution == 'low' or resolution == 'medium' or
                resolution == 'high'):
            wish_item_to_delete = WishList.objects.get(
                user_profile=profile,
                product=ajax_id,
                product_resolution=resolution
            )
        else:
            wish_item_to_delete = WishList.objects.get(
                user_profile=profile,
                product=ajax_id
            )

        # Delete record
        wish_item_to_delete.delete()
        WishList.objects.all().order_by('-id')
        messages.success(request, 'Product deleted from wish list')

        return HttpResponse(status=200)

    # Show an error if item cannot be removed.
    # Alert user with Django message.
    except Exception as e:
        messages.error(request, f'Error removing item_ {e}')
        messages.error(request, 'Exception ocurred')
        return HttpResponse(status=500)
