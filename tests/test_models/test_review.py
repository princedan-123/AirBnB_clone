#!/usr/bin/python3
"""
module for testing user class
"""
import unittest
import pep8
from models.review import Review

class TestUser(unittest.TestCase):
    """
    class user
    """

    def test_pep8_Compliance(self):
        """
        test PEP complaince
        """ 
        file_path = "models/review.py"
        style_guide = pep8.StyleGuide(quiet=True)
        result = style_guide.check_files([file_path])
        self.assertEqual(result.total_errors, 0, f"pep8 errors: {result.total_errors}")

    def test_user_attributes(self):
        """
        testing attributes
        """
        instance = Review()
        self.assertTrue(hasattr(instance, 'place_id'))
        self.assertTrue(hasattr(instance, 'user_id'))
        self.assertTrue(hasattr(instance, 'text'))
        self.assertIsInstance(instance.place_id, str)
        self.assertIsInstance(instance.user_id, str)
        self.assertIsInstance(instance.text, str)


if __name__ == '__main__':
    unittest.main()

