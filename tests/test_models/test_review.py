#!/usr/bin/python3
"""Unittest for Review class
"""

import unittest
import pep8
from models.base_model import BaseModel
from models.review import Review
import json
import os


class TestReview(unittest.TestCase):
    """Test for Review"""

    @classmethod
    def setUpClass(cls):
        """Instances for testing on"""
        cls.r1 = Review()
        cls.r1.place_id = "PlaceId"
        cls.r1.user_id = "UserId"
        cls.r1.text = "Some text goes here."

    @classmethod
    def tearDownClass(cls):
        """Tears down the instances"""
        del cls.r1
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_style(self):
        """Tests Pep8 style"""
        pep = pep8.StyleGuide(quiet=True)
        p = pep.check_files(["models/review.py",
                             "tests/test_models/test_review.py"])
        self.assertEqual(p.total_errors, 0, "PEP8 Errors")

    def test_existence(self):
        """Do all required functions exist?"""
        self.assertTrue(hasattr(Review, "__str__"))
        self.assertTrue(hasattr(Review, "save"))
        self.assertTrue(hasattr(Review, "to_dict"))
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(hasattr(Review, "user_id"))
        self.assertTrue(hasattr(Review, "text"))

    def test_docs(self):
        """Is everything documented?"""
        self.assertTrue(Review.__doc__)

    def test_class(self):
        """Tests that the class type is correct"""
        self.assertTrue(type(self.r1), "<class 'models.review.Review'>")

    def test_is_subclass(self):
        """Tests to see if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_basic(self):
        """Test basic functionality of class"""
        # Test instance creation
        self.assertIsInstance(self.r1, Review)
        self.assertTrue(hasattr(self.r1, "place_id"))
        self.assertTrue(hasattr(self.r1, "user_id"))
        self.assertTrue(hasattr(self.r1, "text"))

        # Test that values are as intended
        self.assertIsInstance(self.r1.place_id, str)
        self.assertIsInstance(self.r1.user_id, str)
        self.assertIsInstance(self.r1.text, str)

    def test_save(self):
        """Test if instance can be saved"""
        self.r1.save()
        self.assertNotEqual(self.r1.created_at, self.r1.updated_at)

    def test_to_dict(self):
        """ Pass """
        r1_dict = self.r1_dict.to_dict()
        self.assertEqual(self.r1_dict.__class__.__name__, "Review")
        self.assertIsInstance(r1_dict["created_at"], str)
        self.assertIsInstance(r1_dict["updated_at"], str)
        self.assertIsInstance(r1_dict["text"], str)


if __name__ == "__main__":
    unittest.main()
