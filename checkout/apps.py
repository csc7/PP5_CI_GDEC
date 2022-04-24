###############################################################################

"""
Python apps file for the Django checkout app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.apps import AppConfig

# INTERNAL:

###############################################################################


class CheckoutConfig(AppConfig):
    """
    Configuration class for the checkout app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
