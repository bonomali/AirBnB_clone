#!/usr/bin/python3
"""Unittest for Base_model class
"""
import unittest
import pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for Base Model"""

    @classmethod
    def setUpClass(cls):
        """Instances for testing on"""
        cls.base1 = BaseModel()
        cls.base1.name = "Holberton"
        cls.base1.my_number = 89
        cls.base2 = BaseModel()
        cls.base2.name = "Betty"
        cls.base2.my_number = 98

    @classmethod
    def tearDownClass(cls):
        """Tears down the instances"""
        del cls.base1
        del cls.base2

    def test_style(self):
        """Tests Pep8 style"""
        pep = pep8.StyleGuide(quiet=True)
        p = pep.check_files(["models/base_model.py",
                             "tests/test_models/test_base_model.py"])
        self.assertEqual(p.total_errors, 0, "PEP8 Errors")

    def test_existence(self):
        """Do all required functions exist?"""
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_docs(self):
        """Is everything documented?"""
        self.assertTrue(BaseModel.__doc__)
        self.assertTrue(BaseModel.__init__.__doc__)
        self.assertTrue(BaseModel.save.__doc__)
        self.assertTrue(BaseModel.to_dict.__doc__)

    def test_basic(self):
        """Test basic functionality of class"""
        # Test instance creation
        self.assertIsInstance(self.base1, BaseModel)
        self.assertTrue(hasattr(self.base1, "id"))
        self.assertNotEqual(self.base1, self.base2)
        self.assertEqual(self.base1.created_at, self.base1.updated_at)

        # Test that values are strings as intended
        self.assertIsInstance(self.base1.id, str)

    def save(self):
        """Test if instance can be saved"""
        self.base1.save()
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)

    def to_dict(self):
        """Test that a dictionary containing all keys/values of __dict__ of the
        instance is returned"""
        base1_dict = self.base1.to_dict()
        self.assertEqual(self.base1.__class__.__name__, "BaseModel")
        self.assertIsInstance(base1_dict["created_at"], str)
        self.assertIsInstance(base1_dict["updated_at"], str)
