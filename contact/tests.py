###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.test import TestCase
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# INTERNAL:
import unittest
from .forms import ContactForm
from .models import DataFromContactForm

###############################################################################


class TestContactApp(unittest.TestCase):
    """
    Class for testing the contact form
    """

    def test_contact_app(self):
        """
        This function creates a record for testing the form
        """
        test_form_data = {
            '2022-01-01',
            '22:22:22',
            'Jkl',
            'test@testemail.com',
            'Test description'
        }
        test_form = ContactForm(test_form_data)
        self.assertTrue(test_form.is_valid())


    def setUp(self):
        print("setUp")
        user = User.objects.get(username='admin2')
        # Get date in Python, copied on January 12th, 2022, at 18:40, from
        # https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python
        self.test_form_data_to_test = DataFromContactForm(
            "datetime.today().strftime('%Y-%m-%d')",
            "22:22:22",
            'Abc Def',
            'Ghi@ghi.com',
            'Text in description'
        )

    @classmethod
    def setUpTestData(cls):
        user = User.objects.get(username=username)

    def tearDown(self):
        print("tearDown")

    def test_full_name_in_contact_form(self):
        self.assertEqual(self.test_form_data_to_test.full_name,
                         'Abc Def')

    def test_email_in_contact_form(self):
        self.assertEqual(self.test_form_data_to_test.email,
                         'Ghi@ghi.com')

    def test_description_in_contact_form(self):
        self.assertEqual(self.test_form_data_to_test.email,
                         'Text in description'
                         )


if __name__ == '__main__':
    unittest.main()