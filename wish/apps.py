###############################################################################

"""
Python apps file for the Django home app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.apps import AppConfig

# INTERNAL:

###############################################################################


class WishConfig(AppConfig):
    """
    Configuration class for the wish app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wish'
