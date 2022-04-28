###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django import forms

# INTERNAL:
from .models import DataFromContactForm

###############################################################################


# Reference: Django Project.
# https://docs.djangoproject.com/en/4.0/topics/forms/


class ContactForm(forms.ModelForm):
    """
    Class for a Simple Contact Form with Django
    """

    # Definition based on this article:
    # https://studygyaan.com/django/
    # how-to-use-bootstrap-4-forms-with-django-crispy-forms#html-code,
    # StudyGyaan, accessed on April 16th, 2022.
    class Meta:
        model = DataFromContactForm
        fields = ('full_name', 'email', 'description')
