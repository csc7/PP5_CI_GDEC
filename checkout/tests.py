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
            'user_name',          # user_profile
            '1',                  # order_number
            2,                    # (Foreign key)
            'full_test_name',     # full_name
            'a@a.com',            # email
            '12345',              # phone_number
            'country_name',       # country
            '98765',              # postcode
            'city_name',          # town_or_city
            'street_1',           # street_address1
            'street_2',           # street_address2
            'county_name',        # county
            '2022-01-01',         # date
            10,                   # delivery_cost
            100,                  # order_total
            110,                  # grand_total
            'original_bag_name',  # original_ban
            'AB12CD34'            # stripe_pid
        )
        self.test_data_for_order_line_item = OrderLineItem(
            '1',                  # (Foreign key)
            '1',                  # (Foreign key)
            '1',                  # order
            'product_resolution', # product_resolution
            10,                   # quantity
            20                    # lineitem_total
        )


    def tearDown(self):
        print("tearDown")


    # Test of Order model return
    def test_order_model_return(self):
        print("Testing return of order number generation")
        self.assertEqual(str(self.test_data_for_order),
                         '1'
                         )

    # Test of Order model elements
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

    def test_phone_number_in_order_model(self):
        print("Testing phone number in Order model")
        self.assertEqual(str(self.test_data_for_order.phone_number),
                         '12345'
                         )

    def test_country_in_order_model(self):
        print("Testing country in Order model")
        self.assertEqual(str(self.test_data_for_order.country),
                         'country_name'
                         )

    def test_postcode_in_order_model(self):
        print("Testing postcode in Order model")
        self.assertEqual(str(self.test_data_for_order.postcode),
                         '98765'
                         )

    def test_town_or_city_number_in_order_model(self):
        print("Testing town or city in Order model")
        self.assertEqual(str(self.test_data_for_order.town_or_city),
                         'city_name'
                         )

    def test_street_address1_in_order_model(self):
        print("Testing street (part 1) in Order model")
        self.assertEqual(str(self.test_data_for_order.street_address1),
                         'street_1'
                         )

    def test_street_address2_in_order_model(self):
        print("Testing street (part 2) in Order model")
        self.assertEqual(str(self.test_data_for_order.street_address2),
                         'street_2'
                         )

    def test_county_in_order_model(self):
        print("Testing county in Order model")
        self.assertEqual(str(self.test_data_for_order.county),
                         'county_name'
                         )

    def test_date_in_order_model(self):
        print("Testing date in Order model")
        self.assertEqual(str(self.test_data_for_order.date),
                         '2022-01-01'
                         )

    def test_delivery_cost_in_order_model(self):
        print("Testing delivery cost in Order model")
        self.assertEqual(str(self.test_data_for_order.delivery_cost),
                         '10'
                         )
                         
    def test_order_total_in_order_model(self):
        print("Testing order total in Order model")
        self.assertEqual(str(self.test_data_for_order.order_total),
                         '100'
                         )

    def test_grand_total_in_order_model(self):
        print("Testing grand total in Order model")
        self.assertEqual(str(self.test_data_for_order.grand_total),
                         '110'
                         )

    def test_original_bag_in_order_model(self):
        print("Testing original bag in Order model")
        self.assertEqual(str(self.test_data_for_order.original_bag),
                         'original_bag_name'
                         )

    def test_stripe_pid_in_order_model(self):
        print("Testing stripe PID in Order model")
        self.assertEqual(str(self.test_data_for_order.stripe_pid),
                         'AB12CD34'
                         )

    # Test of OrderLineItem model elements
    def test_product_resolution_in_order_line_item_model(self):
        print("Testing order number in OrderLineItem model")
        self.assertEqual(str(self.test_data_for_order_line_item.product_resolution),
                         'product_resolution'
                         )

    def test_quantity_in_order_line_item_model(self):
        print("Testing quantity in OrderLineItem model")
        self.assertEqual(str(self.test_data_for_order_line_item.quantity),
                         '10'
                         )

    def test_lineitem_total_in_order_line_item_model(self):
        print("Testing line item total in OrderLineItem model")
        self.assertEqual(str(self.test_data_for_order_line_item.lineitem_total),
                         '20'
                         )


if __name__ == '__main__':
    unittest.main()
