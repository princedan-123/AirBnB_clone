#!/usr/bin/python3
""" A module that serves as a storage for the application """
import os
import json


class FileStorage:
    """ A class that serves as storage, it serializes instances to a JSON file
        and deserializes JSON file back to pythonic objects. it enables newly
        created objects to be served and retrieved for persistency
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """adds newly created objects to the dictionary __objects"""
        name = obj.__class__.__name__
        obj_id = obj.id
        key = "{}.{}".format(name, obj_id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file whose file path is contained
            in the variable __file_path
        """
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes __objects to in JSON file to __objects
            os module is used to check for the existence of the file
            this is done to avoid exception that may arise if file does
            not exist
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
