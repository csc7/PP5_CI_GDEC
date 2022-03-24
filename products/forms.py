###############################################################################

"""
Django forms for the product app, to add, update and delete products
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django import forms

# INTERNAL:
from .models import Product, Category

###############################################################################


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-dark rounded-0'