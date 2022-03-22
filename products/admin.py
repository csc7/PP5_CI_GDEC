###############################################################################

"""
Python administration file for the Django products app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.contrib import admin

# INTERNAL:
from .models import Product, Category

###############################################################################


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image_name',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)