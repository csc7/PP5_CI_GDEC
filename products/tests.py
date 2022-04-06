###############################################################################

"""
Testing for the products app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.test import TestCase
from django.db import models
from datetime import datetime

# INTERNAL:
import unittest
from .models import Category, Product

###############################################################################


class TestProductApp(unittest.TestCase):
    """
    Class for testing the Product app
    """

    def setUp(self):
        print("setUp")
        self.test_data_for_category_model = Category(
            '1',                            # user_profile
            'category_name',                # name
            'category_friendly_name'        # friendly_name
        )

        self.test_data_for_product_model = Product(
            '1',                            # (Foreign key)
            '1',                            # id
            '1',                            # sku
            'product_name',                 # name
            'product_description',          # description
            'product_price',                # price
            'product_resolution',           # resolution
            'product_rating',              # rating
            'product_image_url',            # image_url
            'product_image_name'            # image_name
        )


    def tearDown(self):
        print("tearDown")


    # Test of Category model return
    def test_category_model_return(self):
        print("Testing the return of category model instantiation")
        self.assertEqual(str(self.test_data_for_category_model),
                         'category_name'
                         )

    # Test of Category model elements
    def test_name_in_category_model(self):
        print("Testing name in category model")
        self.assertEqual(str(self.test_data_for_category_model.name),
                         'category_name'
                         )

    def test_friendly_name_in_category_model(self):
        print("Testing friendly name in category model")
        self.assertEqual(str(self.test_data_for_category_model.friendly_name),
                         'category_friendly_name'
                         )


    # Test of Product model return
    def test_product_model_return(self):
        print("Testing the return of product model instantiation")
        self.assertEqual(str(self.test_data_for_product_model),
                         'product_name'
                         )

    # Test of Product model elements
    def test_name_in_product_model(self):
        print("Testing name in product model")
        self.assertEqual(str(self.test_data_for_product_model.name),
                         'product_name'
                         )

##

    def test_sku_in_product_model(self):
        print("Testing SKU in product model")
        self.assertEqual(str(self.test_data_for_product_model.sku),
                         '1'
                         )

    def test_description_in_product_model(self):
        print("Testing description in product model")
        self.assertEqual(str(self.test_data_for_product_model.description),
                         'product_description'
                         )

    def test_price_in_product_model(self):
        print("Testing price in product model")
        self.assertEqual(str(self.test_data_for_product_model.price),
                         'product_price'
                         )

    def test_resolution_in_product_model(self):
        print("Testing resolution in product model")
        self.assertEqual(str(self.test_data_for_product_model.resolution),
                         'product_resolution'
                         )

    def test_rating_in_product_model(self):
        print("Testing rating in product model")
        self.assertEqual(str(self.test_data_for_product_model.rating),
                         'product_rating'
                         )

    def test_image_url_in_product_model(self):
        print("Testing image URL in product model")
        self.assertEqual(str(self.test_data_for_product_model.image_url),
                         'product_image_url'
                         )

    def test_image_name_in_product_model(self):
        print("Testing image name in product model")
        self.assertEqual(str(self.test_data_for_product_model.image_name),
                         'product_image_name'
                         )
            



if __name__ == '__main__':
    unittest.main()