###############################################################################

"""
Python apps file for the Django products app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.apps import AppConfig

# INTERNAL:


###############################################################################


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
