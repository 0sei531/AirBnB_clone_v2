#!/usr/bin/python3
"""This is the city class"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place


class City(BaseModel, Base):
    """This is the class for City"""
    __tablename__ = "cities"
    
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="city")

    def __init__(self, *args, **kwargs):
        """Initializes City object."""
        super().__init__(*args, **kwargs)


