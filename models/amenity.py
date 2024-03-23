#!/usr/bin/python3
"""This is the Amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """This class represents an Amenity.

    Attributes:
        name (str): The name of the Amenity.
        place_amenities (relationship): Relationship to Place model via
                                        place_amenity association table.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)

    def __init__(self, *args, **kwargs):
        """Initialize Amenity object"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Return string representation of Amenity"""
        return "[{}] {}".format(self.__class__.__name__, self.name)

