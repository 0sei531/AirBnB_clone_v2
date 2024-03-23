#!/usr/bin/python3
"""Test cases for Amenity class"""
import unittest
import pycodestyle
from unittest.mock import patch
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
from os import getenv
from time import sleep

storage_t = getenv("HBNB_TYPE_STORAGE")


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def test_is_subclass(self):
        """Test that Amenity is a subclass of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name_attr(self):
        """Test that Amenity has the attribute name, initially set to an empty string"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        if storage_t == 'db':
            self.assertEqual(amenity.name, None)
        else:
            self.assertEqual(amenity.name, "")

    def test_to_dict_creates_dict(self):
        """Test that the to_dict method creates a dictionary with proper attributes"""
        am = Amenity()
        new_d = am.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in am.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Test that values in the dictionary returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = Amenity()
        new_d = am.to_dict()
        self.assertEqual(new_d["__class__"], "Amenity")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], am.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], am.updated_at.strftime(t_format))

    def test_str(self):
        """Test that the __str__ method has the correct output"""
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))

    @patch('models.storage')
    def test_save_method(self, mock_storage):
        """Test the save method and check if it updates"""
        instance5 = Amenity()
        created_at = instance5.created_at
        sleep(2)
        updated_at = instance5.updated_at
        instance5.save()
        new_created_at = instance5.created_at
        sleep(2)
        new_updated_at = instance5.updated_at
        self.assertNotEqual(updated_at, new_updated_at)
        self.assertEqual(created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)

    def test_user_id_and_created_at(self):
        """Test id generation and created_at time for each Amenity instance"""
        amenity_1 = Amenity()
        sleep(2)
        amenity_2 = Amenity()
        sleep(2)
        amenity_3 = Amenity()
        sleep(2)
        list_amenities = [amenity_1, amenity_2, amenity_3]
        for instance in list_amenities:
            amenity_id = instance.id
            with self.subTest(amenity_id=amenity_id):
                self.assertIs(type(amenity_id), str)
        self.assertNotEqual(amenity_1.id, amenity_2.id)
        self.assertNotEqual(amenity_1.id, amenity_3.id)
        self.assertNotEqual(amenity_2.id, amenity_3.id)
        self.assertTrue(amenity_1.created_at <= amenity_2.created_at)
        self.assertTrue(amenity_2.created_at <= amenity_3.created_at)
        self.assertNotEqual(amenity_1.created_at, amenity_2.created_at)
        self.assertNotEqual(amenity_1.created_at, amenity_3.created_at)
        self.assertNotEqual(amenity_3.created_at, amenity_2.created_at)

    def test_instance(self):
        """Check if Amenity is an instance of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(issubclass(type(amenity), BaseModel))
        self.assertEqual(str(type(amenity)), "<class 'models.amenity.Amenity'>")


class TestPEP8(unittest.TestCase):
    """Test for PEP8 style"""

    def test_pep8_conformance(self):
        """Test that the code complies with PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(
            result.total_errors, 0, "Found style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()

