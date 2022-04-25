###############################################################################

"""
Python apps file for the Django profiles app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.apps import AppConfig

# INTERNAL:

###############################################################################


class ProfilesConfig(AppConfig):
    """
    Configuration class for the profiles app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
