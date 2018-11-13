#!/usr/bin/python3
"""Unittest for City class
"""

import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
import json


class TestCity(unittest.TestCase):
    """Test for City"""

    @classmethod
    def setUpClass(cls):
        """Instances for testing on"""
        cls.c1 = City()
        cls.c1.name = "San Francisco"
        cls.c1.state_id = "CA"

        cls.c2 = City()
        cls.c2.name = "Boston"
        cls.c2.state_id = "MA"

    @classmethod
    def tearDownClass(cls):
        """Tears down the instances"""
        del cls.c1
        del cls.c2

    def test_style(self):
        """Tests Pep8 style"""
        pep = pep8.StyleGuide(quiet=True)
        p = pep.check_files(["models/city.py",
                             "tests/test_models/test_city.py"])
        self.assertEqual(p.total_errors, 0, "PEP8 Errors")

    def test_existence(self):
        """Do all required functions exist?"""
        self.assertTrue(hasattr(City, "__str__"))
        self.assertTrue(hasattr(City, "save"))
        self.assertTrue(hasattr(City, "to_dict"))
        self.assertTrue(hasattr(City, "name"))
        self.assertTrue(hasattr(City, "state_id"))

    def test_docs(self):
        """Is everything documented?"""
        self.assertTrue(City.__doc__)

    def test_class(self):
        """Tests that the class type is correct"""
        self.assertTrue(type(self.c1),
                        "<class 'models.city.City'>")

    def test_is_subclass(self):
        """Tests to see if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_basic(self):
        """Test basic functionality of class"""
        # Test instance creation
        self.assertIsInstance(self.c1, City)
        self.assertTrue(hasattr(self.c1, "name"))
        self.assertTrue(hasattr(self.c1, "state_id"))
        self.assertNotEqual(self.c1, self.c2)
        self.assertNotEqual(self.c1.id, self.c2.id)

        # Test that values are strings as intended
        self.assertIsInstance(self.c1.name, str)
        self.assertIsInstance(self.c1.state_id, str)

    def to_dict(self):
        """ Pass """
        c1_dict = self.c1_dict.to_dict()
        self.assertEqual(self.c1_dict.__class__.__name__, "City")
        self.assertIsInstance(c1_dict["created_at"], str)
        self.assertIsInstance(c1_dict["updated_at"], str)

if __name__ == "__main__":
    unittest.main()
