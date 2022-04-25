###############################################################################

"""
Python administration file for the Django wish app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.contrib import admin

# INTERNAL:
from .models import WishList

###############################################################################


# Register your models here.
class WishListAdmin(admin.ModelAdmin):
    """ 
    Class to visualize wish lists in Django admin
    """
    list_display = (
        'user_profile',
        'product',
        'product_resolution',
        'quantity',
        'lineitem_total',
    )

    ordering = ('user_profile',)


admin.site.register(WishList, WishListAdmin)
