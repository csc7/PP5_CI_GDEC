###############################################################################

"""
Django views for the checkout app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

# INTERNAL:
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order

###############################################################################



# Create your views here.

def profile(request):
    """ Display User Profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile details updated successfully')


    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True # To avoid showing bag in success message
                                # after updating profile details, variable
                                # sent to success message toast
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    View for the order history
    """
    
    order = get_object_or_404(Order, order_number=order_number)
    messages.info(request, (
        f'This is a confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }
    return render(request, template, context)