#!/usr/bin/python3
"""
unit testing module
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
import pep8

class TestBaseModel(unittest.TestCase):
    """
    testing the BaseModel class
    """
    def test_pep8_Compliance(self):
        """
        test PEP complaince
        """
        file_path = "models/base_model.py"
        style_guide = pep8.StyleGuide(quiet=True)
        result = style_guide.check_files([file_path])
        self.assertEqual(result.total_errors, 0, f"pep8 errors: {result.total_errors}")

    def test_init(self):
        """
        testing the initialization
        """
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_str(self):
        """
        testing string method
        """
        instance = BaseModel()
        str_representation = str(instance)
        self.assertIn(instance.__class__.__name__, str_representation)
        self.assertIn(instance.id, str_representation)

    def test_save(self):
        """
        testing the save method
        """
        instance = BaseModel()
        first_update = instance.updated_at
        instance.save()
        second_update = instance.updated_at
        self.assertNotEqual(first_update, second_update)

    def test_to_dict(self):
        """
        testing the dict method
        """
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertIn('__class__', instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)

if __name__ == '__main__':
    unittest.main()

