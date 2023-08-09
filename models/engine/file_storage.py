#!/usr/bin/python3
"""the FileStorage class."""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with
        key <obj class name>.id
        """
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj
