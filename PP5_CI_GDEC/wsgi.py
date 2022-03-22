###############################################################################

"""
WSGI config for PP5_CI_GDEC project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
import os
from django.core.wsgi import get_wsgi_application

# INTERNAL:

###############################################################################


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PP5_CI_GDEC.settings')

application = get_wsgi_application()
