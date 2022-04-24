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
    This function computes the grand total amount based on the products
    in the bag and the user's delivery preferences

    Parameters In: HTTP request object

    Parameters Out: context with variables to process the bag purchase
    amounts:
        'bag_items'
        'order_total'
        'order_product_count'
        'delivery'
        'delta_for_discount'
        'discount_threshold'
        'grand_total'
        'discount'
        'discount_percentage'
        'cancel_delivery_cost'
    """

    # Check if user has activated the option to receive the data
    # digitally and therefore cancel delivery costs
    if request.method == 'POST':
        cancel_delivery_cost = request.POST.get('digital', False)
        if cancel_delivery_cost:
            cancel_delivery_cost_factor = 0
        else:
            cancel_delivery_cost_factor = 1

    else:
        cancel_delivery_cost = request.POST.get('digital', False)
        if cancel_delivery_cost:
            cancel_delivery_cost_factor = 0
        else:
            cancel_delivery_cost_factor = 1


    # Initialize bag item and costs amounts
    bag_items = []
    order_total = 0
    order_product_count = 0
    bag = request.session.get('bag', {})

    # Iterate elements in the bag, accounting for item, quantity, product
    # and, if applies, resolution 
    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            
            product = get_object_or_404(Product, pk=item_id)
            order_total += item_data * product.price
            order_product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for resolution, quantity in item_data['items_by_resolution'].items():
                order_total += quantity * product.price
                order_product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'resolution': resolution,
                })

    # Compute grand total
    if order_total < settings.DISCOUNT_THRESHOLD:
        delivery = order_total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
        delivery = delivery * cancel_delivery_cost_factor
        discount = 0
        delta_for_discount = Decimal(settings.DISCOUNT_THRESHOLD) - order_total
        
    else:
        delivery = order_total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
        delivery = delivery * cancel_delivery_cost_factor
        discount = order_total * Decimal(settings.DISCOUNT_PERCENTAGE/100)
        delta_for_discount = 0
        
    grand_total = order_total + delivery - discount

    # Return context to bag template
    context = {
        'bag_items': bag_items,
        'order_total': order_total,
        'order_product_count': order_product_count,
        'delivery': delivery,
        'delta_for_discount': delta_for_discount,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
        'grand_total': grand_total,
        'discount': discount,
        'discount_percentage': settings.DISCOUNT_PERCENTAGE,
        'cancel_delivery_cost': cancel_delivery_cost,
    }

    return context