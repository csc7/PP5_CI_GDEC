###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from crispy_forms.layout import Layout, Submit, Row, Column

# INTERNAL:
from .models import DataFromContactForm

###############################################################################


# Reference: Django Project.
# https://docs.djangoproject.com/en/4.0/topics/forms/


class ContactForm(forms.ModelForm):
    """
    Class for a Simple Contact Form with Django
    """
    
    # Definition based on this article: https://studygyaan.com/django/how-to-use-bootstrap-4-forms-with-django-crispy-forms#html-code,
    # StudyGyaan, accessed on April 16th, 2022.
    class Meta:
        model = DataFromContactForm
        fields = ('full_name', 'email', 'description')

    #full_name = forms.CharField(label='Full Name', max_length=50)
    #email = forms.EmailField(label='E-Mail', max_length=100, required=False)
    #description = forms.TextField(label='Description', max_length=2000)

    #helper = FormHelper()
    #helper.label_class = 'col-lg-6'  
    #helper.field_class = 'col-lg-6'  

    
    #def __init__(self, *args, **kwargs):
    #    super(DataFromContactForm, self).__init__(*args,**kwargs)
    #    self.helper = FormHelper()
    #    self.helper.form_class = 'form-horizontal'
    #    self.helper.label_class = 'col-lg-2'  
    #    self.helper.field_class = 'col-lg-8'
    #    self.helper.form_tag = False
    #    self.helper.layout = Layout(
    #        Field('full_name'),
    #        Field('email', style='max-width: 1em'),
    #        Field('description'),
    #        )