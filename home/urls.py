###############################################################################

"""
Django URLs for the home app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.urls import path

# INTERNAL:
from .import views

###############################################################################


# URLs resulting from the bag app
urlpatterns = [
    path('', views.index, name='home'),
    path('gdpr_privacy_policy/', views.gdpr_privacy_policy,
         name='gdpr_privacy_policy'),
    path('gdpr_cookies/', views.gdpr_cookies, name='gdpr_cookies'),
]