#!/usr/bin/python3
"""This module defines a class BaseModel"""
import uuid
from datetime import datetime


class BaseModel:
    """This class defines a Base Model
    Attributes:
    id (string): id number assigned when an instance is created
    created_at (datetime): assigned with the current datetime when an instance is created
    updated_at (datetime): assigned with the current datetime when an instance is created and is will be updated every time the object is changed
    """

    def __init__(self):
        """Initialization of BaseModel
        Args:
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Prints the class name, id, and a dictionary representation
        """
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Updates updated_at with the current datetime
        Returns:
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance
        Returns:
        """
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
