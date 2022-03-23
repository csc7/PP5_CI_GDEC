###############################################################################

"""
Django views for the checkout app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.shortcuts import render, get_object_or_404

# INTERNAL:
from .models import UserProfile
from .forms import UserProfileForm


###############################################################################



# Create your views here.

def profile(request):
    """ Display User Profile """
    profile = get_object_or_404(UserProfile, user=request.user)


    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)