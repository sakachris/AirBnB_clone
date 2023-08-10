#!/usr/bin/python3
"""
models/user.py module for user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Inherits BaseModel and creates new users
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
