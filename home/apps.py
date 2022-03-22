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


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
