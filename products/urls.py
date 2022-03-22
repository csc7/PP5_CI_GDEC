###############################################################################

"""
Django URLs for the products app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.urls import path

# INTERNAL:
from .import views

###############################################################################


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
]