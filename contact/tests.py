###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.test import TestCase
from django.db import models
from datetime import datetime

# INTERNAL:
import unittest
from .forms import ContactForm
from .models import DataFromContactForm

###############################################################################


class TestContactForm(unittest.TestCase):
    """
    Class for testing the contact form
    """

    def test_contact_form(self):
        """
        This function creates a record for testing the form
        """
        test_form_data = {
            'name': 'Abc',
            'surname': 'Def',
            'email': 'Ghi@ghi.com',
            'text_content': 'Test description'
        }
        test_form = ContactForm(test_form_data)
        self.assertTrue(test_form.is_valid())

    def setUp(self):
        print("setUp")
        # Get date in Python, copied on January 12th, 2022, at 18:40, from
        # https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python
        self.test_form_data_to_test = DataFromContactForm(
            datetime.today().strftime('%Y-%m-%d'),
            "22:22:22",
            'Abc',
            'Def',
            'Ghi@ghi.com',
            'Text in description'
        )

    def tearDown(self):
        print("tearDown")

    def test_name_in_contact_form(self):
        self.assertEqual(self.test_form_data_to_test.name, 'Def')

    def test_surname_in_contact_form(self):
        self.assertEqual(self.test_form_data_to_test.time, 'Abc')

    def test_email_in_contact_form(self):
        self.assertEqual(self.test_form_data_to_test.surname, 'Ghi@ghi.com')

    def test_description_in_contact_form(self):
        self.assertEqual(self.test_form_data_to_test.email,
                         'Text in description'
                         )


if __name__ == '__main__':
    unittest.main()