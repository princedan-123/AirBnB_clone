#!/usr/bin/python3
"""A module for the city class """
from .base_model import BaseModel


class City(BaseModel):
    """city class to indicate the city and it is a subclass of Basemodel"""
    state_id = ""
    name = ""
