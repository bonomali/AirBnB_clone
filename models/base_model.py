#!/usr/bin/python3
"""This module defines a class BaseModel"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """This class defines a Base Model
    """

    def __init__(self, *args, **kwargs):
        """Initialization of BaseModel
        Attributes:
        id (string): id number assigned when an instance is created
        created_at (datetime): assigned with the current datetime when an instance
        is created
        updated_at (datetime): assigned with the current datetime when an instance
        is created and it will be updated every time the object is changed
        """
        format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
            if "id" in kwargs.keys():
                self.id = kwargs["id"]
            if "created_at" in kwargs.keys():
                self.created_at = datetime.strptime(kwargs["created_at"],
                                                    format)
            if "updated_at" in kwargs.keys():
                self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                    format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Prints the class name, id, and a dictionary representation
        Returns:
            A string representation of the class name, id, and dict
        """
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__))

    def save(self):
        """Updates updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the
        instance
        Returns:
            A dictionary with the specified keys included
        """
        dicts = self.__dict__.copy()
        dicts["__class__"] = self.__class__.__name__
        dicts["created_at"] = self.created_at.isoformat()
        dicts["updated_at"] = self.updated_at.isoformat()
        return dicts
