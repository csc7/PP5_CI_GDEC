###############################################################################

"""
Python apps file for the Django bag app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.apps import AppConfig

# INTERNAL:

###############################################################################


class BagConfig(AppConfig):
    """ 
    Configuration class for the bag app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
