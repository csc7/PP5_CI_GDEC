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


# URLs resulting from the bag app
urlpatterns = [
    path('', views.all_products, name='products'),
    # Specify integer for product_id URL to avoid "add/" (in the next URL)
    # being interpreted as a product ID, resulting in an error
    path('<int:product_id>', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/',
         views.delete_product, name='delete_product'),
    path('product_review/<int:product_id>/',
         views.product_review, name='product_review'),
    path('delete_product_review/<int:product_id>/<int:comment_id>/',
         views.delete_product_review, name='delete_product_review'),
]
