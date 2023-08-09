#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
""" This module contains a superclass BaseModel that will be inherited"""
class BaseModel:
    """A super class that subsquent classes will inherit from """
    def __init__(self, *args, **kwargs):
        """the object constructor, it initialises instances of BaseModel"""
        if kwargs and len(args) == 0:
            for i in kwargs.keys():
                if i == created_at:
                    obj_format = datetime.fromisoformat(i)
                    self.i = obj_format
                elif i == updated_at:
                    obj_format = datetime.fromisoformat(i)
                    self.i = obj_format
                elif i != __class__ :
                    self.i = kwargs[i]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    def __str__(self):
        """returns the string representation of the class BaseModel"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    def save(self):
        """updates the public instance attribute updated_at 
            with the current datetime"""
        self.updated_at = datetime.now()
    def to_dict(self):
        """returns a dictionary containing all keys/values 
            of __dict__ of the instance"""
        dic = self.__dict__
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
