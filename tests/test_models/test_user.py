#!/usr/bin/python3
"""Unittest for User class
"""

import unittest
import pep8
from models.base_model import BaseModel
from models.user import User
import json


class TestUser(unittest.TestCase):
    """Test for User"""

    @classmethod
    def setUpClass(cls):
        """Instances for testing on"""
        cls.u1 = User()
        cls.u1.first_name = "Betty"
        cls.u1.last_name = "Holberton"
        cls.u1.email = "BettyH@email.com"
        cls.u1.password = "1234"

        cls.u2 = User()
        cls.u2.first_name = "John"
        cls.u2.last_name = "Doe"
        cls.u2.email = "JD@email.com"
        cls.u2.password = "54321"

    @classmethod
    def tearDownClass(cls):
        """Tears down the instances"""
        del cls.u1
        del cls.u2

    def test_style(self):
        """Tests Pep8 style"""
        pep = pep8.StyleGuide(quiet=True)
        p = pep.check_files(["models/user.py",
                             "tests/test_models/test_user.py"])
        self.assertEqual(p.total_errors, 0, "PEP8 Errors")

    def test_existence(self):
        """Do all required functions exist?"""
        self.assertTrue(hasattr(User, "__str__"))
        self.assertTrue(hasattr(User, "save"))
        self.assertTrue(hasattr(User, "to_dict"))
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))

    def test_docs(self):
        """Is everything documented?"""
        self.assertTrue(User.__doc__)

    def test_class(self):
        """Tests that the class type is correct"""
        self.assertTrue(type(self.u1), "<class 'models.user.User'>")

    def test_is_subclass(self):
        """Tests to see if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_basic(self):
        """Test basic functionality of class"""
        # Test instance creation
        self.assertIsInstance(self.u1, User)
        self.assertTrue(hasattr(self.u1, "first_name"))
        self.assertTrue(hasattr(self.u1, "last_name"))
        self.assertTrue(hasattr(self.u1, "email"))
        self.assertTrue(hasattr(self.u1, "password"))
        self.assertNotEqual(self.u1, self.u2)
        self.assertNotEqual(self.u1.id, self.u2.id)

        # Test that values are strings as intended
        self.assertIsInstance(self.u1.first_name, str)
        self.assertIsInstance(self.u1.last_name, str)
        self.assertIsInstance(self.u1.password, str)
        self.assertIsInstance(self.u1.email, str)

    def to_dict(self):
        """ Pass """
        u1_dict = self.u1_dict.to_dict()
        self.assertEqual(self.u1_dict.__class__.__name__, "User")
        self.assertIsInstance(u1_dict["created_at"], str)
        self.assertIsInstance(u1_dict["updated_at"], str)

if __name__ == "__main__":
    unittest.main()
