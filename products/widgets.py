###############################################################################

"""
Widget to improve the image view of products when managing/administering the
database, based on an inherited class, ClearableFileInput(FileInput) of Django
that is later customized below.
"""

# IMPORTED RESOURCES #

# EXTERNAL:
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _

# INTERNAL:

###############################################################################


# Copied and modified from Code Institute "Boutique Ado" project
# on March 24th, 2022, at 18:35


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'