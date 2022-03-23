###############################################################################

"""
Django views for the checkout app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.shortcuts import render

# INTERNAL:


###############################################################################



# Create your views here.

def profile(request):
    """ Display User Profile """
    
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)