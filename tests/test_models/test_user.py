#!/usr/bin/python3
"""
module for testing user class
"""
import unittest
import pep8
from models.user import User

class TestUser(unittest.TestCase):
    """
    class user
    """

    def test_pep8_Compliance(self):
        """
        test PEP complaince
        """ 
        file_path = "models/user.py"
        style_guide = pep8.StyleGuide(quiet=True)
        result = style_guide.check_files([file_path])
        self.assertEqual(result.total_errors, 0, f"pep8 errors: {result.total_errors}")

    def test_user_attributes(self):
        """
        testing attributes
        """
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

if __name__ == '__main__':
    unittest.main()

