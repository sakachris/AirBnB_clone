#!/usr/bin/python3
"""Defines the Review class."""
from base_model import BaseModel


class Review(BaseModel):
    """represents the customer's review"""
    place_id = ""
    user_id = ""
    text = ""
