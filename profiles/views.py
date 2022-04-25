###############################################################################

"""
Django views for the checkout app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

# INTERNAL:
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from django.contrib.auth.decorators import login_required

###############################################################################


# Use Django login decorator to access this view
@login_required()
def profile(request):
    """ Display User Profile
    
    Parameters In: HTTP request object

    Parameters Out: request object, template to profiles/profile.html, and
    context variables:
        'form',
        'orders',
        'do_not_show_bag_in_toast'
    
    """

    # Read profile
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile details updated successfully')

    # Read orders from user
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    # Template to return
    template = 'profiles/profile.html'

    # Context variables to return
    context = {
        'form': form,
        'orders': orders,
        'do_not_show_bag_in_toast': True # To avoid showing bag in success
                                         # message after updating profile
                                         # details, variable sent to success
                                         # message toast
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    View for the order history

    Parameters In: HTTP request object, order number

    Parameters Out: request object,
        template to checkout/checkout_success.html, and
        context variables:
            'form',
            'from_profile'
    """
    
    # Read order
    order = get_object_or_404(Order, order_number=order_number)

    # Template to return
    template = 'checkout/checkout_success.html'

    # Context variables to return
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)