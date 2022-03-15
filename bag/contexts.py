from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.DISCOUNT_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        delta_for_discount = settings.DISCOUNT_THRESHOLD - total
    else:
        delivery = total * Decimal((settings.STANDARD_DELIVERY_PERCENTAGE / 2) / 100)
        delta_for_discount = 0
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'delta_for_discount': delta_for_discount,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
        'grand_total': grand_total,
    }

    return context