#!/usr/bin python3
"""
models/engine/file_storage.py for JSON serialization & deserialization
"""
from os.path import isfile
from json import dump, load
import sys


class FileStorage:
    """
<<<<<<< HEAD
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
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects.update({key: obj})

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        j_dict = {}
        for key, val in FileStorage.__objects.items():
            j_dict.update({key: val.to_dict()})
        with open(FileStorage.__file_path, mode='w', encoding='UTF-8') as f:
            dump(j_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects if it exists
        """
        from models import base_model
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding='UTF-8') as file:
                from_json = load(file)
                for val in from_json.values():
                    cls_name = val["__class__"]
                    cls_obj = getattr(base_model, cls_name)
                    self.new(cls_obj(**val))
