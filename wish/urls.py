###############################################################################

"""
Django URLs for the wish list app
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
    path('', views.view_wish_list, name='view_wish_list'),
    path('add_to_wish_list/<item_id>/', views.add_to_wish_list, name='add_to_wish_list'),
    path('adjust_wish_list/<item_id>/', views.adjust_wish_list, name='adjust_wish_list'),
    path('remove_from_wish_list/<item_id>/', views.remove_from_wish_list, name='remove_from_wish_list'),

]