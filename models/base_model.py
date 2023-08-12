#!/usr/bin/python3
"""
Module for the base class of the project
"""
from uuid import uuid4
from datetime import datetime
from models import storage
# from models.engine.file_storage import FileStorage


class BaseModel:
    """
    defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """ Initializing BaseModel class """
        if kwargs:
            attr = {k: v for k, v in kwargs.items() if k != '__class__'}
            for key, val in attr.items():
                if key in ['created_at', 'updated_at']:
                    dt_obj = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, dt_obj)
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Implementing string output """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """ updates updated_at with the current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """  returns a dictionary of the object instance """
        dt = {}
        dt["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if type(val) == datetime:
                dt[key] = val.isoformat()
            else:
                dt[key] = val
        return dt
