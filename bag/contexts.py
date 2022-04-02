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



def bag_contents(request):
    """
    Function
    """

    if request.method == 'POST':
        cancel_delivery_cost = request.POST.get('digital', False)
        if cancel_delivery_cost:
            cancel_delivery_cost_factor = 0
        else:
            cancel_delivery_cost_factor = 1
        print(cancel_delivery_cost)

    else:
        cancel_delivery_cost = request.POST.get('digital', False)
        if cancel_delivery_cost:
            cancel_delivery_cost_factor = 0
        else:
            cancel_delivery_cost_factor = 1
        print(cancel_delivery_cost)


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
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
        delivery = delivery * cancel_delivery_cost_factor
        discount = 0
        delta_for_discount = settings.DISCOUNT_THRESHOLD - total
    else:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
        delivery = delivery * cancel_delivery_cost_factor
        discount = total * Decimal(settings.DISCOUNT_PERCENTAGE/100)
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
        'cancel_delivery_cost': cancel_delivery_cost,
    }

    return context