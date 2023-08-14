#!/usr/bin/python3
"""
module for testing user class
"""
import unittest
import pep8
from models.place import Place


class TestUser(unittest.TestCase):
    """
    class user
    """

    def test_pep8_Compliance(self):
        """
        test PEP complaince
        """
        file_path = "models/place.py"
        style_guide = pep8.StyleGuide(quiet=True)
        result = style_guide.check_files([file_path])
        self.assertEqual(result.total_errors, 0,
                         f"pep8 errors: {result.total_errors}")

    def test_user_attributes(self):
        """
        testing attributes
        """
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, str)


if __name__ == '__main__':
    unittest.main()
