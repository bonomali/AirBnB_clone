#!/usr/bin/python3
"""Unittest for State class
"""

import unittest
import pep8
from models.base_model import BaseModel
from models.state import State
import json


class TestState(unittest.TestCase):
    """Test for State"""

    @classmethod
    def setUpClass(cls):
        """Instances for testing on"""
        cls.s1 = State()
        cls.s1.name = "California"

    @classmethod
    def tearDownClass(cls):
        """Tears down the instances"""
        del cls.s1

    def test_style(self):
        """Tests Pep8 style"""
        pep = pep8.StyleGuide(quiet=True)
        p = pep.check_files(["models/state.py",
                             "tests/test_models/test_state.py"])
        self.assertEqual(p.total_errors, 0, "PEP8 Errors")

    def test_existence(self):
        """Do all required functions exist?"""
        self.assertTrue(hasattr(State, "__str__"))
        self.assertTrue(hasattr(State, "save"))
        self.assertTrue(hasattr(State, "to_dict"))
        self.assertTrue(hasattr(State, "name"))

    def test_docs(self):
        """Is everything documented?"""
        self.assertTrue(State.__doc__)

    def test_class(self):
        """Tests that the class type is correct"""
        self.assertTrue(type(self.s1),
                        "<class 'models.state.State'>")

    def test_is_subclass(self):
        """Tests to see if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_basic(self):
        """Test basic functionality of class"""
        # Test instance creation
        self.assertIsInstance(self.s1, State)
        self.assertTrue(hasattr(self.s1, "name"))

        # Test that values are strings as intended
        self.assertIsInstance(self.s1.name, str)

    def to_dict(self):
        """ Pass """
        s1_dict = self.s1_dict.to_dict()
        self.assertEqual(self.s1_dict.__class__.__name__, "State")
        self.assertIsInstance(s1_dict["created_at"], str)
        self.assertIsInstance(s1_dict["updated_at"], str)

if __name__ == "__main__":
    unittest.main()
