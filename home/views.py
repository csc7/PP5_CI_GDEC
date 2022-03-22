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
    """View for index page"""

    return render(request, 'home/index.html')
