#!/usr/bin/python3
"""Test suite for State class"""

import unittest
import os
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def __init__(self, *args, **kwargs):
        """Initialize the test class"""
        super().__init__(*args, **kwargs)
        self.state = State()
        self.state.name = "State"

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.state = State()
        cls.state.name = "CA"

    @classmethod
    def tearDownClass(cls):
        """At the end of the test, tear it down"""
        del cls.state

    def tearDown(self):
        """Tear down"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_checking_for_docstring_state(self):
        """Check for docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_attributes_state(self):
        """Check if State has attributes"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_is_subclass_state(self):
        """Test if State is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attribute_types_state(self):
        """Test attribute type for State"""
        self.assertEqual(type(self.state.name), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', 'Not file engine')
    def test_save_state(self):
        """Test if the save method works"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict_state(self):
        """Test if to_dict method works"""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()

