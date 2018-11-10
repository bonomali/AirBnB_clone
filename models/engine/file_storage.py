#!/usr/bin/python3
"""This module defines a class FileStorage"""
import json
from models.base_model import BaseModel

class FileStorage:
    """This class defines how File Storage works
    Attributes:
    file_path (string): path to the JSON file
    objects (dict): stores all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Gives the dictionary __objects
        Returns:
            The dict __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        Args:
            obj: the object
        """
        clas = obj.__class__.__name__
        id = obj.id
        FileStorage.__objects[clas + "." + id] = obj

    def save(self):
        """Serializes __objects to the JSON file
        """
        dicts = {}
        for key, value in FileStorage.__objects.items():
            dicts[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(dicts, file)

    def reload(self):
        """Deserializes __objects from the JSON file
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                fload = json.load(file)
                for key, value in fload.items():
                    self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
