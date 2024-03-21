#!/usr/bin/python3
"""Test suite for Review class"""

import unittest
import os
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.review = Review()
        cls.review.place_id = "4321-dcba"
        cls.review.user_id = "123-bca"
        cls.review.text = "The strongest in the Galaxy"

    @classmethod
    def tearDownClass(cls):
        """At the end of the test, tear it down"""
        del cls.review

    def tearDown(self):
        """Tear down"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_checking_for_docstring_review(self):
        """Check for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_review(self):
        """Check if review has attributes"""
        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('text' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)

    def test_is_subclass_review(self):
        """Test if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def test_attribute_types_review(self):
        """Test attribute types for Review"""
        self.assertEqual(type(self.review.text), str)
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', 'Not file engine')
    def test_save_review(self):
        """Test if the save method works"""
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_to_dict_review(self):
        """Test if to_dict method works"""
        self.assertEqual('to_dict' in dir(self.review), True)


if __name__ == "__main__":
    unittest.main()

