#!/usr/bin/python3
"""
module for testing user class
"""
import unittest
import pep8
from models.amenity import Amenity


class TestUser(unittest.TestCase):
    """
    class user
    """

    def test_pep8_Compliance(self):
        """
        test PEP complaince
        """
        file_path = "models/amenity.py"
        style_guide = pep8.StyleGuide(quiet=True)
        result = style_guide.check_files([file_path])
        self.assertEqual(result.total_errors, 0,
                         f"pep8 errors: {result.total_errors}")

    def test_amenity(self):
        """
        testing amenity
        """
        instance = Amenity()
        self.assertTrue(hasattr(instance, 'name'))
        self.assertIs(instance.name, str)


if __name__ == '__main__':
    unittest.main()
