#!/usr/bin/python3
"""Unit tests for console module"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test suite for the console module"""

    @classmethod
    def setUpClass(cls):
        """Set up the test"""
        cls.console = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """Tear down the test"""
        del cls.console

    def tearDown(self):
        """Remove temporary file (file.json) created as a result"""
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            try:
                os.remove("file.json")
            except FileNotFoundError:
                pass

    def test_docstrings_in_console(self):
        """Check for docstrings"""
        self.assertIsNotNone(__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)

    def test_emptyline(self):
        """Test empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual('', f.getvalue())


if __name__ == "__main__":
    unittest.main()

