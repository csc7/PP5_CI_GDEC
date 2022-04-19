###############################################################################

"""
Django signals for the checkout app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# INTERNAL:
from. models import OrderLineItem

###############################################################################


@receiver (post_save, sender=OrderLineItem, weak=True)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total in checkout items
    """
    instance.order.update_total()

@receiver (post_delete, sender=OrderLineItem, weak=True)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total in checkout items
    """
    print('Delete signal received')
    instance.order.update_total()