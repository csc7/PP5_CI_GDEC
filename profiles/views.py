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