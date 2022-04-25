###############################################################################

"""
Django models for the products app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.db import models

# INTERNAL:
from profiles.models import User

###############################################################################


# Copied and modified from Code Institute "Boutique Ado" project
# on March 2nd, 2022, at 16:00

class Category(models.Model):
    """
    Django Category Model
    """
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Django Product Model
    """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    resolution = models.BooleanField(default=False, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image_name = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


# To add a comment feature:
# copied and modified (except RATING VALUES) 
# from https://djangocentral.com/creating-comments-system-with-django/,
# Abhijeet Pal, Author and Editor in Chief @djangocentral,
# on April 12th, 2022.
class ProductComment(models.Model):
    """
    Django Product Comment Model
    """
    class Meta:
        ordering = ['created_on']

    # To limit field content to specific values,
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/,
    # accessed on April 12th, 2022.
    RATING_VALUES = [
        (5, 'Fantastic'),
        (4, 'Good'),
        (3, 'Average'),
        (2, 'Poor'),
        (1, 'Very Poor'),
    ]

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_rating_value = models.IntegerField(choices=RATING_VALUES, default=5)

    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user)