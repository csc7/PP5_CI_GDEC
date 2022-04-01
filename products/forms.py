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
from products.widgets import CustomClearableFileInput

###############################################################################


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('category', 'sku', 'name', 'description', 'price', 'resolution', 'rating', 'image_name', )

    image_name = forms.ImageField(label='Image name', required=False, widget=CustomClearableFileInput)
    #image_url = forms.URLField(label='Image url', required=False, initial='')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-dark rounded-0'