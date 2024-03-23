#!/usr/bin/python3
"""Test cases for the City class"""

import unittest
import os
import pycodestyle
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test suite for the City class"""

    @classmethod
    def setUpClass(cls):
        """Set up test fixtures"""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def tearDownClass(cls):
        """Clean up after the test"""
        del cls.city

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8(self):
        """Test PEP8 compliance for city.py"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(
            result.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_docstrings(self):
        """Check for docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes(self):
        """Test presence of attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass(self):
        """Test if City is a subclass of BaseModel"""
        self.assertTrue(
            issubclass(self.city.__class__, BaseModel),
            "City is not a subclass of BaseModel"
        )

    def test_attribute_types(self):
        """Test attribute types for City"""
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)

    def test_save(self):
        """Test if save method works"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        """Test if to_dict method returns dictionary"""
        self.assertEqual('to_dict' in dir(self.city), True)


class TestPEP8(unittest.TestCase):
    """Test PEP8 compliance for the city module"""

    def test_pep8(self):
        """Test PEP8 compliance for city.py"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(
            result.total_errors, 0,
            "Found code style errors (and warnings)."
        )


if __name__ == "__main__":
    unittest.main()

