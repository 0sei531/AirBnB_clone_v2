#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models


class State(BaseModel, Base):
    """This is the class for State"""

    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """Return the list of associated cities"""
        return [city for city in models.storage.all(City).values()
                if city.state_id == self.id]

