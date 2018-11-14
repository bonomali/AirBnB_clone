#!/usr/bin/python3
"""Unittest for Place class
"""
import os
import unittest
import pep8
from models.base_model import BaseModel
from models.place import Place
import json


class TestPlace(unittest.TestCase):
    """Test for Place"""

    @classmethod
    def setUpClass(cls):
        """Instances for testing on"""
        cls.p1 = Place()
        cls.p1.city_id = "City"
        cls.p1.user_id = "User"
        cls.p1.name = "UserName"
        cls.p1.description = "A nice place to stay"
        cls.p1.number_rooms = 0
        cls.p1.number_bathrooms = 0
        cls.p1.max_guest = 0
        cls.p1.price_by_night = 0
        cls.p1.latitude = 0.0
        cls.p1.longitude = 0.0
        cls.p1.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        """Tears down the instances"""
        del cls.p1
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_style(self):
        """Tests Pep8 style"""
        pep = pep8.StyleGuide(quiet=True)
        p = pep.check_files(["models/place.py",
                             "tests/test_models/test_place.py"])
        self.assertEqual(p.total_errors, 0, "PEP8 Errors")

    def test_existence(self):
        """Do all required functions exist?"""
        self.assertTrue(hasattr(Place, "__str__"))
        self.assertTrue(hasattr(Place, "save"))
        self.assertTrue(hasattr(Place, "to_dict"))
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "amenity_ids"))

    def test_docs(self):
        """Is everything documented?"""
        self.assertTrue(Place.__doc__)

    def test_class(self):
        """Tests that the class type is correct"""
        self.assertTrue(type(self.p1), "<class 'models.place.Place'>")

    def test_is_subclass(self):
        """Tests to see if Place is a subclass of BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_basic(self):
        """Test basic functionality of class"""
        # Test instance creation
        self.assertIsInstance(self.p1, Place)
        self.assertTrue(hasattr(self.p1, "city_id"))
        self.assertTrue(hasattr(self.p1, "user_id"))
        self.assertTrue(hasattr(self.p1, "name"))
        self.assertTrue(hasattr(self.p1, "description"))
        self.assertTrue(hasattr(self.p1, "number_rooms"))
        self.assertTrue(hasattr(self.p1, "number_bathrooms"))
        self.assertTrue(hasattr(self.p1, "max_guest"))
        self.assertTrue(hasattr(self.p1, "price_by_night"))
        self.assertTrue(hasattr(self.p1, "latitude"))
        self.assertTrue(hasattr(self.p1, "longitude"))
        self.assertTrue(hasattr(self.p1, "amenity_ids"))

        # Test that values are as intended
        self.assertIsInstance(self.p1.city_id, str)
        self.assertIsInstance(self.p1.user_id, str)
        self.assertIsInstance(self.p1.name, str)
        self.assertIsInstance(self.p1.description, str)
        self.assertIsInstance(self.p1.number_rooms, int)
        self.assertIsInstance(self.p1.number_bathrooms, int)
        self.assertIsInstance(self.p1.max_guest, int)
        self.assertIsInstance(self.p1.price_by_night, int)
        self.assertIsInstance(self.p1.latitude, float)
        self.assertIsInstance(self.p1.longitude, float)
        self.assertIsInstance(self.p1.amenity_ids, list)

    def test_save(self):
        """Test if instance can be saved"""
        self.p1.save()
        self.assertNotEqual(self.p1.created_at, self.p1.updated_at)

    def test_to_dict(self):
        """ Pass """
        p1_dict = self.p1.to_dict()
        self.assertEqual(self.p1.__class__.__name__, "Place")
        self.assertIsInstance(p1_dict["created_at"], str)
        self.assertIsInstance(p1_dict["updated_at"], str)
