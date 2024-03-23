#!/usr/bin/python3
"""Test cases for the Place class"""

from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import pycodestyle


class TestPlace(test_basemodel):
    """Test suite for the Place class"""

    def __init__(self, *args, **kwargs):
        """Initialize test instance"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Test if city_id attribute is of type str"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Test if user_id attribute is of type str"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Test if name attribute is of type str"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Test if description attribute is of type str"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Test if number_rooms attribute is of type int"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Test if number_bathrooms attribute is of type int"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Test if max_guest attribute is of type int"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Test if price_by_night attribute is of type int"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Test if latitude attribute is of type float"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Test if longitude attribute is of type float"""
        new = self.value()
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """Test if amenity_ids attribute is of type list"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)


class TestPEP8(unittest.TestCase):
    """Test PEP8 compliance for place.py"""

    def test_pep8(self):
        """Test PEP8 compliance for place.py"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(
            result.total_errors, 0,
            "Found code style errors (and warnings)."
        )


if __name__ == "__main__":
    unittest.main()

