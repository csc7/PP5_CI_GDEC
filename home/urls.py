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


urlpatterns = [
    path('', views.index, name='home'),
    path('gdp_privacy_policy/', views.gdpr_privacy_policy, name='gdp_-privacy_policy'),
]