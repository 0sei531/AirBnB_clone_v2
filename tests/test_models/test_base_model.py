#!/usr/bin/python3
"""Unit tests for BaseModel class"""
import unittest
import datetime
import json
import os
import pycodestyle
import inspect
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Set up for test"""
        cls.base = BaseModel()
        cls.base.name = "Kev"
        cls.base.num = 20

    @classmethod
    def tearDownClass(cls):
        """Tear down after test"""
        del cls.base

    def tearDown(self):
        """Clean up after each test method"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """Test PEP8 compliance"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 style issues")

    def test_docstrings_BaseModel(self):
        """Test presence of docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_methods_BaseModel(self):
        """Test existence of expected methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_instance_BaseModel(self):
        """Test instance creation"""
        self.assertIsInstance(self.base, BaseModel)

    def test_save_method(self):
        """Test save method"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method"""
        base_dict = self.base.to_dict()
        self.assertEqual(base_dict['__class__'], 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

    def test_uuid_generation(self):
        """Test UUID generation"""
        instance1 = BaseModel()
        instance2 = BaseModel()
        instance3 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)
        self.assertNotEqual(instance1.id, instance3.id)
        self.assertNotEqual(instance2.id, instance3.id)

    def test_str_method(self):
        """Test __str__ method"""
        string_output = "[BaseModel] ({}) {}".format(self.base.id, self.base.__dict__)
        self.assertEqual(string_output, str(self.base))


class TestCodeFormat(unittest.TestCase):
    """Test code formatting with PEP8"""
    def test_pep8_conformance(self):
        """Test that models/base_model.py conforms to PEP8"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 style issues")


class TestDocstrings(unittest.TestCase):
    """Test docstrings"""
    def test_docstrings_presence(self):
        """Test presence of docstrings"""
        self.assertTrue(BaseModel.__doc__)
        self.assertTrue(BaseModel.__init__.__doc__)
        self.assertTrue(BaseModel.__str__.__doc__)
        self.assertTrue(BaseModel.save.__doc__)
        self.assertTrue(BaseModel.to_dict.__doc__)


if __name__ == "__main__":
    unittest.main()

