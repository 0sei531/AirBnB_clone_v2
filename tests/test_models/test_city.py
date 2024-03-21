#!/usr/bin/python3
"""Test suite for the City class"""

import unittest
import os
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    @classmethod
    def setUpClass(cls):
        """Set up the test"""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def tearDownClass(cls):
        """Tear down the test"""
        del cls.city

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_checking_for_docstring(self):
        """Check if docstrings are present"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes(self):
        """Check if City has attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass(self):
        """Test if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attribute_types(self):
        """Test attribute types for City"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', 'Not file engine')
    def test_save(self):
        """Test if save method works"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        """Test if to_dict method works"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()

