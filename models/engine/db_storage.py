#!/usr/bin/python3
"""This module defines the DBStorage class for AirBnB"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base


class DBStorage:
    """The DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization method for DBStorage instances"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user, pwd, host, db), pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of all objects"""
        from models import classes
        session = self.__session
        all_objs = {}

        if cls:
            objs = session.query(classes[cls]).all()
        else:
            objs = []
            for cls in classes.values():
                objs += session.query(cls).all()

        for obj in objs:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            all_objs[key] = obj

        return all_objs

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and creates the current database session"""
        Base.metadata.create_all(bind=self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """Call remove() method on the private session attribute"""
        self.__session.close()

