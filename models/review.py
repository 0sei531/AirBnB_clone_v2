#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models import storage_type

class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = 'reviews'

    if storage_type == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def text(self):
            """Get the review text."""
            return self.text

        @property
        def place_id(self):
            """Get the place id."""
            return self.place_id

        @property
        def user_id(self):
            """Get the user id."""
            return self.user_id

        @text.setter
        def text(self, value):
            """Set the review text."""
            self.text = value

        @place_id.setter
        def place_id(self, value):
            """Set the place id."""
            self.place_id = value

        @user_id.setter
        def user_id(self, value):
            """Set the user id."""
            self.user_id = value

