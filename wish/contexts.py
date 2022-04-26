###############################################################################

"""
Context file for the bag app, computing grand total and delivery costs.
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

# INTERNAL:
from products.models import Product

###############################################################################


def wish_list_contents(request):
    """
    This function computes the quantities and price per item
    in the wish list

    Parameters In: HTTP request object, product ID

    Parameters Out: context variables to wish list template:
        'wish_list_items_',
        'total_',
        'product_count_'
    """

    # Initialize wish list items and costs amounts
    wish_list_items = []
    total = 0
    product_count = 0
    wish_list = request.session.get('wish_list', {})

    # Iterate elements in the bag, accounting for item, quantity, product
    # and, if applies, resolution
    for item_id, item_data in wish_list.items():
        if isinstance(item_data, int):

            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            wish_list_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for (resolution, quantity) in (
                    item_data['items_by_resolution'].items()
                    ):
                total += quantity * product.price
                product_count += quantity
                wish_list_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'resolution': resolution,
                })

    # Return context to bag template
    context = {
        'wish_list_items_': wish_list_items,
        'total_': total,
        'product_count_': product_count,
    }

    return context
