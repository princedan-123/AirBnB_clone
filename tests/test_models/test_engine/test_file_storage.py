#!/usr/bin/python3
"""
unit testing
"""

import unittest
import os
import pep8
import json
from models.base_model import BaseModel
from models.engine.filestorage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    testing FileStorage class
    """
    def setUp(self):
        """
        runs before each test
        """
        self.file_path = "file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        """
        runs after each test
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """
        tests the all method of the class
        """
        self.assertIsInstance(self.storage.all(), dict)
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """
        testing the new method of the class
        """
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def test_save_and_reload(self):
        """
        test the save and reload methods
        """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, new_storage.all())


if __name__ == "__main__":
    unittest.main()
