#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass
        storage._FileStorage__objects = {}

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_empty_initial_storage(self):
        """ Check if storage dictionary is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new_object_added(self):
        """ Check if a new object is correctly added to storage """
        new_object = BaseModel()
        stored_objects = storage.all().values()
        self.assertTrue(new_object in stored_objects)

    def test_all_method_returns_dict(self):
        """ Check if the all() method returns a dictionary """
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_save_creates_file(self):
        """ Check if the save method creates the storage file """
        new_object = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload_from_empty_file(self):
        """ Check if reloading from an empty file raises ValueError """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_empty_storage(self):
        """ Check if reloading an empty storage works correctly """
        new_object = BaseModel()
        storage.save()
        storage.reload()
        self.assertEqual(len(storage.all()), 1)

    def test_base_model_save(self):
        """ Check if BaseModel save method calls storage save """
        new_object = BaseModel()
        new_object.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_file_path_type(self):
        """ Check if __file_path attribute is a string """
        self.assertIsInstance(storage._FileStorage__file_path, str)

    def test_objects_type(self):
        """ Check if __objects attribute is a dictionary """
        self.assertIsInstance(storage.all(), dict)

    def test_key_format(self):
        """ Check if keys in storage are properly formatted """
        new_object = BaseModel()
        _id = new_object.to_dict()['id']
        key = 'BaseModel.' + _id
        self.assertIn(key, storage.all().keys())

    def test_storage_instance(self):
        """ Check if storage is an instance of FileStorage """
        from models.engine.file_storage import FileStorage
        self.assertIsInstance(storage, FileStorage)


if __name__ == "__main__":
    unittest.main()

