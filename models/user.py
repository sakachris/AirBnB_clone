#!/usr/bin/python3
"""Defines the User class."""
from base_model import BaseModel


class User(BaseModel):
    """defines a  user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
