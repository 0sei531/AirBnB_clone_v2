#!/usr/bin/python3
""" Module for SQL Alchemy-based database storage """

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """ Class for SQL Alchemy-based database storage """

    __engine = None
    __session = None

    def __init__(self):
        """ Initializes database connection """
        user = getenv("HBNB_MYSQL_USER", "root")
        passwd = getenv("HBNB_MYSQL_PWD", "")
        db = getenv("HBNB_MYSQL_DB", "hbnb_dev_db")
        host = getenv("HBNB_MYSQL_HOST", "localhost")
        env = getenv("HBNB_ENV", "production")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returns a dictionary of all objects """
        dic = {}
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            classes = [State, City, User, Place, Review, Amenity]
            for cls in classes:
                query = self.__session.query(cls)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return dic

    def new(self, obj):
        """ Adds a new object to the session """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes to the database """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes an object from the session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Reloads objects from the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ Closes the session """
        self.__session.close()

