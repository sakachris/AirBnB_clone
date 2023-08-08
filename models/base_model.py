#!/usr/bin/python3
"""
Module for the base class of the project
"""
from uuid import uuid4
from datetime import datetime


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

    def __str__(self):
        """ Implementing string output """
        return ("[{}] ({}) {}".format(__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """ updates updated_at with the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """  returns a dictionary of the object instance """
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        dt = self.__dict__
        dt["__class__"] = __class__.__name__
        return dt


"""one = BaseModel()
print(one)
print(one.id)
print(type(one.id))
print(one.created_at)
print(type(one.created_at))
print(one.updated_at)
print(type(one.updated_at))
one.save()
print(one)
print(one.to_dict())"""
