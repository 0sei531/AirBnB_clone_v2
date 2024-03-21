#!/usr/bin/python3
"""Test for DBStorage"""
import unittest
from os import getenv
import MySQLdb
from models.engine.db_storage import DBStorage
from models.state import State


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'Not using DB storage')
class TestDBStorage(unittest.TestCase):
    """Test cases for DBStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up connection and storage instance"""
        cls.user = getenv("HBNB_MYSQL_USER")
        cls.password = getenv("HBNB_MYSQL_PWD")
        cls.db_name = getenv("HBNB_MYSQL_DB")
        cls.host = getenv("HBNB_MYSQL_HOST")
        cls.db = MySQLdb.connect(host=cls.host, user=cls.user,
                                 passwd=cls.password, db=cls.db_name,
                                 charset="utf8")
        cls.cursor = cls.db.cursor()
        cls.storage = DBStorage()
        cls.storage.reload()

    @classmethod
    def tearDownClass(cls):
        """Close cursor and database connection"""
        cls.cursor.close()
        cls.db.close()

    def test_read_tables(self):
        """Test if expected tables exist"""
        self.cursor.execute("SHOW TABLES")
        tables = self.cursor.fetchall()
        self.assertTrue(tables)

    def test_no_element_in_users_table(self):
        """Test if the users table is initially empty"""
        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()
        self.assertEqual(len(users), 0)

    def test_no_element_in_cities_table(self):
        """Test if the cities table is initially empty"""
        self.cursor.execute("SELECT * FROM cities")
        cities = self.cursor.fetchall()
        self.assertEqual(len(cities), 0)

    def test_add_state(self):
        """Test adding a state to the database"""
        self.cursor.execute("SELECT * FROM states")
        initial_state_count = len(self.cursor.fetchall())
        state = State(name="California")
        state.save()
        self.storage.save()
        self.cursor.execute("SELECT * FROM states")
        updated_state_count = len(self.cursor.fetchall())
        self.assertEqual(updated_state_count, initial_state_count + 1)


if __name__ == "__main__":
    unittest.main()

