###############################################################################

"""
Python administration file for the Django checkout app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.contrib import admin

# INTERNAL:
from .models import Order, OrderLineItem

###############################################################################


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Class to visualize order line items in Django admin
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Class to visualize orders in Django admin
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total', 'discount',
                       'grand_total', 'original_bag', 'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost', 'discount',
              'order_total', 'grand_total', 'original_bag', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
