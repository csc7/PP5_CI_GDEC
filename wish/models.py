###############################################################################

"""
Django models for the checkout app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings

# INTERNAL:
from products.models import Product
from profiles.models import UserProfile

###############################################################################


# Create your models here.

class WishList(models.Model):
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_wishlist'
    )
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_resolution = models.CharField(max_length=2, null=True, blank=True) # High, medium and low
    quantity = models.IntegerField(null=False, blank=False, default=0)
    # Just to show current price
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def __str__(self):
        return f'Wish list for {self.user_profile}'