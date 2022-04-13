###############################################################################

"""
Django forms for the checkout app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django import forms

# INTERNAL:
from .models import UserProfile

###############################################################################


class UserProfileForm(forms.ModelForm):
    """
    Order Form Class
    """
    class Meta:
        model = UserProfile()
        exclude = ('user',)
        

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {            
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-dark rounded-0'
            if field == 'default_street_address1':
                self.fields[field].label = 'Street Address 1'
            if field == 'default_street_address2':
                self.fields[field].label = 'Street Address 2'
            # Capitalize first letter of each word: https://stackoverflow.com/questions/1549641/how-can-i-capitalize-the-first-letter-of-each-word-in-a-string,
            # accessed on April 14th, 2022, at 01:54
            self.fields[field].label = self.fields[field].label.title()