#!/usr/bin/python3
"""
Console Module
"""
import cmd
import sys
import os
import re
from datetime import datetime
import uuid
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    # Code for HBNBCommand class methods goes here...

if __name__ == "__main__":
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        storage = DBStorage()
    else:
        storage = FileStorage()

    storage.reload()
    HBNBCommand().cmdloop()

