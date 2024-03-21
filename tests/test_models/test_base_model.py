#!/usr/bin/python3
"""Test for BaseModel"""
import unittest
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test suite for the BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Setup for the test"""
        cls.base = BaseModel()
        cls.base.name = "Kev"
        cls.base.num = 20

    @classmethod
    def tearDown(cls):
        """At the end of the test, tear down"""
        del cls.base

    def tearDown(self):
        """Tear down"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_checking_for_docstring_basemodel(self):
        """Check for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_basemodel(self):
        """Check if BaseModel has methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_basemodel(self):
        """Test if the base is an instance of BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', 'Not file engine')
    def test_save_basemodel(self):
        """Test if the save method works"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_basemodel(self):
        """Test if dictionary conversion works"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()

