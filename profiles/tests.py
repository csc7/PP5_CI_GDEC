###############################################################################

"""
Testing for the products app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:

# INTERNAL:
import unittest
from .models import UserProfile

###############################################################################


class TestProfilesApp(unittest.TestCase):
    """
    Class for testing the Product app
    """

    def setUp(self):
        print("setUp")
        self.test_data_for_profiles_model = UserProfile(
            '1',                            # (Foreign key)
            '1',                            # id
            '1234512345',                   # default_phone_number
            'profiles_street_1',            # default_street_address1
            'profiles_street_2',            # default_street_address2
            'profiles_town_or_city',        # default_town_or_city
            'profiles_county',              # default_county
            '1234567890',                   # default_postcode
            'profiles_country'              # default_country
        )

    def tearDown(self):
        print("tearDown")

    # Test of Profiles model elements
    def test_user_in_profiles_model(self):
        print("Testing user in Profiles model")
        self.assertEqual(str(self.test_data_for_profiles_model.user),
                         'admin'
                         )

    def test_default_phone_number_in_profiles_model(self):
        print("Testing phone number in Profiles model")
        self.assertEqual(str(
            self.test_data_for_profiles_model.default_phone_number),
            '1234512345'
        )

    def test_default_street_address1_in_profiles_model(self):
        print("Testing street address (part 1) in Profiles model")
        self.assertEqual(str(
            self.test_data_for_profiles_model.default_street_address1),
            'profiles_street_1'
        )

    def test_default_street_address2_in_profiles_model(self):
        print("Testing street address (part 2) in Profiles model")
        self.assertEqual(str(
            self.test_data_for_profiles_model.default_street_address2),
            'profiles_street_2'
        )

    def test_default_town_or_city_in_profiles_model(self):
        print("Testing town or city in Profiles model")
        self.assertEqual(str(
            self.test_data_for_profiles_model.default_town_or_city),
            'profiles_town_or_city'
        )

    def test_default_county_in_profiles_model(self):
        print("Testing county in Profiles model")
        self.assertEqual(str(
            self.test_data_for_profiles_model.default_county),
            'profiles_county'
        )

    def test_default_postcode_in_profiles_model(self):
        print("Testing postcode in Profiles model")
        self.assertEqual(str(
            self.test_data_for_profiles_model.default_postcode),
            '1234567890'
        )

    def test_default_country_in_profiles_model(self):
        print("Testing country in Profiles model")
        self.assertEqual(str(
            self.test_data_for_profiles_model.default_country),
            'profiles_country'
        )
