#!/usr/bin/python3
"""A module for review class """
from .base_model import BaseModel


class Review(BaseModel):
    """A subclass of BaseModel that represent reviews"""
    place_id = ""
    user_id = ""
    text = ""
