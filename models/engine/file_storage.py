#!/usr/bin/python3
"""This module defines a class FileStorage"""
import json

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
        with open(FileStorage.__file_path, "w") as file:
            json.dump(dicts, file)

    def reload(self):
        """Deserializes __objects from the JSON file
        """
        dicts = {}
        try:
            with open(FileStorage.__file_path, "r") as file:
                    dicts = json.load(file)
                    FileStorage.__objects = {}
                    for key, value in dicts.items():
                        print(value)
        except FileNotFoundError:
            pass
