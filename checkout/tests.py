###############################################################################

"""
Testing for the checkout app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.test import TestCase
from django.db import models
from datetime import datetime

# INTERNAL:
import unittest
from .models import Order, OrderLineItem

###############################################################################


class TestCheckoutApp(unittest.TestCase):
    """
    Class for testing the Checkout app
    """

    def setUp(self):
        print("setUp")
        self.test_data_for_order = Order(
            'user_name',        # user_profile
            '1',                # order_number
            2,                  # (Foreign key)
            'full_test_name',   # full_name
            'a@a.com',          # email
            '12345',
            'country_name',
            '98765',
            'city_name',
            'street_1',
            'streer_2',
            'county_name',
            '2022-01-01',
            10,
            100,
            110,
            'original_bag_name',
            'AB12CD34'
        )
        print(Order)
        self.test_data_for_order_line_item = OrderLineItem(
            'ABCD0001', 
            'product_name',
            'product_resolution',
            10,
            20
        )

    def tearDown(self):
        print("tearDown")


    def test_order_number_in_order_model(self):
        print("Testing order number in Order model")
        self.assertEqual(str(self.test_data_for_order.order_number),
                         '1'
                         )

    def test_user_profile_in_order_model(self):
        print("Testing user profile in Order model")
        self.assertEqual(str(self.test_data_for_order.user_profile),
                         'admin'
                         )

    def test_full_name_in_order_model(self):
        print("Testing full name in Order model")
        self.assertEqual(str(self.test_data_for_order.full_name),
                         'full_test_name'
                         )

    def test_email_in_order_model(self):
        print("Testing email in Order model")
        self.assertEqual(str(self.test_data_for_order.email),
                         'a@a.com'
                         )




if __name__ == '__main__':
    unittest.main()