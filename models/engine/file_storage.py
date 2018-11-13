#!/usr/bin/python3
"""This module defines a class FileStorage"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This class defines how File Storage works
    Attributes:
    file_path (string): path to the JSON file
    objects (dict): stores all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}
    all_classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
                   "City": City, "Place": Place, "Review": Review,
                   "State": State}

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
                    val = FileStorage.all_classes[value["__class__"]](**value)
                    FileStorage.__objects[key] = val
        except FileNotFoundError:
            pass

    def get_obj(cls, id):
        """ Checks the id against objects, the objects in __objects, and if
        there is a match, return the object. """
        obj = cls.__objects
        for value in obj.values():
            if value.id == id:
                return value
        print("No match found.")
