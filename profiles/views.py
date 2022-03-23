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


###############################################################################



# Create your views here.

def profile(request):
    """ Display User Profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)