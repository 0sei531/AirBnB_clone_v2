#!/usr/bin/python3
"""Test cases for the Review class"""

from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class TestReview(test_basemodel):
    """Test suite for the Review class"""

    def __init__(self, *args, **kwargs):
        """Initialize test instance"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test if place_id attribute is of type str"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Test if user_id attribute is of type str"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Test if text attribute is of type str"""
        new = self.value()
        self.assertEqual(type(new.text), str)


if __name__ == "__main__":
    unittest.main()

