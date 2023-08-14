#!/usr/bin/python3
"""A module for the state class"""
from .base_model import BaseModel


class State(BaseModel):
    """ A subclass of BaseModel that indicates the state"""
    name = ""
