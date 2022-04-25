###############################################################################

"""
Django models for the bag app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django import template

# INTERNAL:

###############################################################################


# Call this function to compute the total price per row (subtotal)
register = template.Library()

@register.filter(name="calc_subtotal")
def calc_subtotal(price, quantity):
    """ Compute total per item (subtotal)
    
    Parameters In: price and quantity

    Parameters Out: subtotal (price*quantity)

    """

    return price * quantity