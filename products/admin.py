###############################################################################

"""
Python administration file for the Django products app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.contrib import admin

# INTERNAL:
from .models import Product, Category, ProductComment

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


# To add a comment feature:
# copied and modified from https://djangocentral.com/creating-comments-system-with-django/,
# Abhijeet Pal, Author and Editor in Chief @djangocentral,
# on April 12th, 2022.
#@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('user', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductComment, ProductCommentAdmin)