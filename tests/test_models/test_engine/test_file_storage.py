#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.city import City


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        cls.user = User()
	cls.user.first_name = "Jean-Luc"
        cls.user.last_name = "Picard"
        cls.user.email = "makeitso@hotmail.com"
        cls.storage = FileStorage()

    @classmethod
    def tearDown(cls):
        """ Remove storage file at end of tests """
        del cls.user

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_storage_style(self):
        '''tests pep8'''
        style= pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        '''tests all function'''
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage.__FileStorage__objects)

    def test_new(self):
        '''tests new function'''
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = 1701
        user.name = "Jean-Luc"
        storage.new(user)
        key = user.__class__.__name__ + '.' + str(user.id)
        self.assertIsNotNone(obj[key])

        def test_reload_filestorage(self):
        """test reload function"""
        storage = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(storage.reload(), None)

if __name__ == "__main__":
    unittest.main()
