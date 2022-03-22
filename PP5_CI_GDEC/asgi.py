###############################################################################

"""
ASGI config for PP5_CI_GDEC project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
import os
from django.core.asgi import get_asgi_application

# INTERNAL:

###############################################################################


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PP5_CI_GDEC.settings')

application = get_asgi_application()
