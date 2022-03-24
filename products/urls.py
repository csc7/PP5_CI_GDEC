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
    # Specify integer for product_id URL to avoid "add/" (in the next URL)
    # being interpreted as a product ID, resulting in an error
    path('<int:product_id>', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),

]