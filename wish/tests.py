###############################################################################

"""
Testing for the wish list app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.test import TestCase
from django.db import models
from datetime import datetime

# INTERNAL:
import unittest
from .models import WishList

###############################################################################


class TestWishListApp(unittest.TestCase):
    """
    Class for testing the Wish List app
    """

    def setUp(self):
        print("setUp")

        self.test_data_for_wish_list_model = WishList(
            '50',                           # id
            '1',                            # user profile (foreign key)
            '50',                           # product (foreign key)
            'High',                         # product resolution
            '2',                            # quantity
            '22.33',                        # line item total
        )

    def tearDown(self):
        print("tearDown")

    # Test of WishList model return
    def test_wish_list_model_return(self):
        print("Testing the return of wish list model instantiation")
        self.assertEqual(str(self.test_data_for_wish_list_model),
                         'Wish list for admin'
                         )

    # Test of WishList model elements
    def test_user_profile_in_wish_list_model(self):
        print("Testing user profile in wish list model")
        self.assertEqual(str(self.test_data_for_wish_list_model.user_profile),
                         'admin'
                         )

    def test_product_in_wish_list_model(self):
        print("Testing user profile in wish list model")
        self.assertEqual(str(self.test_data_for_wish_list_model.product),
                         'Vanuatu DEM'
                         )

    def test_product_resolution_in_wish_list_model(self):
        print("Testing user profile in wish list model")
        self.assertEqual(str(
            self.test_data_for_wish_list_model.product_resolution),
            'High'
        )

    def test_quantity_in_wish_list_model(self):
        print("Testing user profile in wish list model")
        self.assertEqual(str(self.test_data_for_wish_list_model.quantity),
                         '2'
                         )

    def test_line_item_total_in_wish_list_model(self):
        print("Testing user profile in wish list model")
        self.assertEqual(str(
            self.test_data_for_wish_list_model.lineitem_total),
            '22.33'
        )


if __name__ == '__main__':
    unittest.main()
