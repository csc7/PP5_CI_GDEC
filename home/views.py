###############################################################################

"""
Django views for the home app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.shortcuts import render

# INTERNAL:

###############################################################################


# Create your views here.

def index(request):
    """View for index page

    Parameters In: HTTP request object

    Parameters Out: request object to home/index.html
    """

    return render(request, 'home/index.html')


def gdpr_privacy_policy(request):
    """View for index page

    Parameters In: HTTP request object

    Parameters Out: request object to home/gdpr_privacy_policy.html
    """

    return render(request, 'home/gdpr_privacy_policy.html')


def gdpr_cookies(request):
    """View for index page
    Parameters In: HTTP request object

    Parameters Out: request object to home/gdpr_cookies.html
    """

    return render(request, 'home/gdpr_cookies.html')
