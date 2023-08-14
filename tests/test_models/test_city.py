#!/usr/bin/python3
"""
module for testing user class
"""
import unittest
import pep8
from models.city import City

class TestUser(unittest.TestCase):
    """
    class user
    """

    def test_pep8_Compliance(self):
        """
        test PEP complaince
        """ 
        file_path = "models/city.py"
        style_guide = pep8.StyleGuide(quiet=True)
        result = style_guide.check_files([file_path])
        self.assertEqual(result.total_errors, 0, f"pep8 errors: {result.total_errors}")

    def test_user_attributes(self):
        """
        testing attributes
        """
        place = City()
        self.assertTrue(hasattr(place, 'state_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertIsInstance(place.state_id, str)
        self.assertIsInstance(place.name, str)


if __name__ == '__main__':
    unittest.main()

