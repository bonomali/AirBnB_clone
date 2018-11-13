#!/usr/bin/python3
"""Unittest for FileStorage class
"""
import unittest
import pep8
import os
import shutil
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test for FileStorage"""

    @classmethod
    def setUpClass(cls):
        """Instances for testing on"""
        cls.user = User()
        cls.user.email = "Holberton@school.com"
        cls.user.password = "password"
        cls.user.first_name = "Betty"
        cls.user.last_name = "Holberton"
        cls.stored = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """Tears down the instances"""
        del cls.user

    def test_style(self):
        """Tests Pep8 style"""
        pep = pep8.StyleGuide(quiet=True)
        p = pep.check_files(["models/engine/file_storage.py"])
        self.assertEqual(p.total_errors, 0, "PEP8 Errors")

    def test_existence(self):
        """Do all required functions exist?"""
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "reload"))


    def test_docs(self):
        """Is everything documented?"""
        self.assertTrue(FileStorage.__doc__)
        self.assertTrue(FileStorage.new.__doc__)
        self.assertTrue(FileStorage.save.__doc__)
        self.assertTrue(FileStorage.reload.__doc__)
        self.assertTrue(FileStorage.all.__doc__)

    def test_all(self):
        """Tests that all gives the dict __objects"""
        instances = self.stored.all()
        self.assertIsNotNone(instances)
        self.assertIsInstance(instances, dict)
        self.assertIs(instances, self.stored._FileStorage__objects)

    def test_new(self):
        """Tests that new sets a new object in __objects"""
        instances = self.stored.all()
        key = self.user.__class__.__name__ + "." + str(self.user.id)
        self.assertIsInstance(self.user, User)
        self.assertIsNotNone(instances[key])

    def reload(self):
        """Tests that reload deserializes the __objects from the JSON file"""
        try:
            os.remove("file.json")
        except Exception:
            pass
        shutil.copy("./tests/test_models/test_engine/example.txt", "./file.json")
        with open("./file.json") as file:
            dictionary = json.load(file)
        self.stored.reload()
        objects = self.stored.all()
        for key in dictionary:
            self.assertEqual(objects[key].to_dict(), dicts[key])
