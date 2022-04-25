###############################################################################

"""
Django URLs for the profiles app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.urls import path

# INTERNAL:
from . import views

###############################################################################


# URLs resulting from the bag app
urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
]
