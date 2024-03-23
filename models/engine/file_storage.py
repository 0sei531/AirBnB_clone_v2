#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
import shlex
from models.base_model import BaseModel


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of objects filtered by class
        Args:
            cls (Class, optional): Class to filter objects. Defaults to None.
        Returns:
            dict: Dictionary of objects filtered by class if cls is provided,
                  otherwise all objects.
        """
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Sets __objects to given obj
        Args:
            obj (BaseModel): Given object
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        my_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="UTF-8") as file_handle:
            json.dump(my_dict, file_handle)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as file_handle:
                obj_dict = json.load(file_handle)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass

    def remove(self, obj=None):
        """Deletes an existing object from __objects
        Args:
            obj (BaseModel, optional): Object to delete. Defaults to None.
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """Calls reload()"""
        self.reload()

