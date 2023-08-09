#!/usr/bin/python3
"""base model class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    It defines all common attributes/methods for other classes
    in the airbnb clone
    """
    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_format)
                else:
                    self.__dict__[k] = v

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dt = self.__dict__.copy()
        dt["created_at"] = self.created_at.isoformat()
        dt["updated_at"] = self.updated_at.isoformat()
        dt["__class__"] = self.__class__.__name__
        return dt

    def __str__(self):
        """returns the string representation of the base class instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
