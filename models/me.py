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

if __name__ == "__main__":
    my_model1 = BaseModel()
    print(my_model1.__dict__)
    dic = my_model1.to_dict()
    print(dic)
    print(my_model1.__dict__)
