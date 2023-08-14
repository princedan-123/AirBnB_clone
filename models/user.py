#!/usr/bin/python3
"""this module creates a class called User"""
from models.base_model import BaseModel


class User(BaseModel):
    """A class that inherits from User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
