#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship

association_table = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 primary_key=True, nullable=False))


class Amenity(BaseModel, Base):
    """Represents an Amenity for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table amenities.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Amenities.
        name (sqlalchemy String): The amenity name.
        place_amenities (sqlalchemy relationship): Place-Amenity relationship.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=association_table,
                                   back_populates="amenities")

