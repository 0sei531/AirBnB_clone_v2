#!/usr/bin/python3
"""Unit tests for Amenity class"""
import unittest
import os
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test suite for the Amenity class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.amenity = Amenity(name="WiFi")

    @classmethod
    def tearDownClass(cls):
        """Tear down the test"""
        del cls.amenity

    def tearDown(self):
        """Remove temporary file (file.json) created as a result"""
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            try:
                os.remove("file.json")
            except FileNotFoundError:
                pass

    def test_attributes(self):
        """Test presence of attributes"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_attribute_types(self):
        """Test attribute types"""
        self.assertIsInstance(self.amenity.name, str)

    def test_is_subclass(self):
        """Test if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_save(self):
        """Test save functionality"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        self.assertTrue('to_dict' in dir(self.amenity))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_name_type(self):
        """Test type of name attribute"""
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity.name, str)


if __name__ == "__main__":
    unittest.main()

