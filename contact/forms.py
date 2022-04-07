###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django import forms

###############################################################################


# Reference: Django Project.
# https://docs.djangoproject.com/en/4.0/topics/forms/


class ContactForm(forms.Form):
    """
    Class for a Simple Contact Form with Django
    """
    full_name = forms.CharField(label='Full Name', max_length=50)
    email = forms.EmailField(label='E-Mail', max_length=100, required=False)
    text_content = forms.CharField(label='Description', max_length=2000)