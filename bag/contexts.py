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
import json
import re

# INTERNAL:
from products.models import Product

###############################################################################


def bag_contents(request):
    """
    Function
    """



    requested_html = re.search(r'^text/html',
                               request.META.get('HTTP_ACCEPT')
                               )

    if not requested_html:
        discount_delivery = json.dumps(request.POST.get('applyDiscount'))[1:-1]
        print(discount_delivery)
    

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for resolution, quantity in item_data['items_by_resolution'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'resolution': resolution,
                })

    if 'product_resolution' in request.POST:
        print("OK")

    if total < settings.DISCOUNT_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        discount = 0
        delta_for_discount = settings.DISCOUNT_THRESHOLD - total
    else:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)        
        discount = total * Decimal(settings.DISCOUNT_PERCENTAGE / 100)
        delta_for_discount = 0
    
    grand_total = total + delivery - discount
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'delta_for_discount': delta_for_discount,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
        'grand_total': grand_total,
        'discount': discount,
        'discount_percentage': settings.DISCOUNT_PERCENTAGE,
    }

    return context