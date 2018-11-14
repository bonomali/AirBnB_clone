#!/usr/bin/python3
"""Unittest for Amenity class
"""

import unittest
import pep8
from models.base_model import BaseModel
from models.amenity import Amenity
import json
import os


class TestAmenity(unittest.TestCase):
    """Test for Amenity"""

    @classmethod
    def setUpClass(cls):
        """Instances for testing on"""
        cls.amenity1 = Amenity()
        cls.amenity1.name = "Pool Table"
        cls.amenity2 = Amenity()
        cls.amenity2.name = "Pool"

    @classmethod
    def tearDownClass(cls):
        """Tears down the instances"""
        del cls.amenity1
        del cls.amenity2
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_style(self):
        """Tests Pep8 style"""
        pep = pep8.StyleGuide(quiet=True)
        p = pep.check_files(["models/amenity.py",
                             "tests/test_models/test_amenity.py"])
        self.assertEqual(p.total_errors, 0, "PEP8 Errors")

    def test_existence(self):
        """Do all required functions exist?"""
        self.assertTrue(hasattr(Amenity, "__str__"))
        self.assertTrue(hasattr(Amenity, "save"))
        self.assertTrue(hasattr(Amenity, "to_dict"))
        self.assertTrue(hasattr(Amenity, "name"))

    def test_docs(self):
        """Is everything documented?"""
        self.assertTrue(Amenity.__doc__)

    def test_class(self):
        """Tests that the class type is correct"""
        self.assertTrue(type(self.amenity1),
                        "<class 'models.amenity.Amenity'>")

    def test_is_subclass(self):
        """Tests to see if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_basic(self):
        """Test basic functionality of class"""
        # Test instance creation
        self.assertIsInstance(self.amenity1, Amenity)
        self.assertTrue(hasattr(self.amenity1, "name"))
        self.assertNotEqual(self.amenity1, self.amenity2)
        self.assertNotEqual(self.amenity1.id, self.amenity2.id)

        # Test that values are strings as intended
        self.assertIsInstance(self.amenity1.name, str)

    def test_save(self):
        """Test if instance can be saved"""
        self.amenity1.save()
        self.assertNotEqual(self.amenity1.created_at, self.amenity1.updated_at)

    def test_to_dict(self):
        """ Pass """
        am1_dict = self.amenity1.to_dict()
        self.assertEqual(self.amenity1.__class__.__name__, "Amenity")
        self.assertIsInstance(am1_dict["created_at"], str)
        self.assertIsInstance(am1_dict["updated_at"], str)
