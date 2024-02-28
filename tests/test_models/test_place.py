#!/usr/bin/python3
"""unittest of the Place Class"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    This class contains unit tests for the Place class.
    """

    def test_attributes(self):
        """
        Test the default attributes of a Place instance.
        """
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_init(self):
        """
        Test the initialization of a Place instance with custom attributes.
        """
        place = Place(city_id="123", user_id="456", name="Test Place")
        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.user_id, "456")
        self.assertEqual(place.name, "Test Place")

    def test_attribute_types(self):
        """
        Test the types of attributes in a Place instance.
        """
        self.assertIsInstance(self.place1.city_id, str)
        self.assertIsInstance(self.place1.user_id, str)
        self.assertIsInstance(self.place1.name, str)
        self.assertIsInstance(self.place1.description, str)
        self.assertIsInstance(self.place1.number_rooms, int)
        self.assertIsInstance(self.place1.number_bathrooms, int)
        self.assertIsInstance(self.place1.max_guest, int)
        self.assertIsInstance(self.place1.price_by_night, int)
        self.assertIsInstance(self.place1.latitude, float)
        self.assertIsInstance(self.place1.longitude, float)
        self.assertIsInstance(self.place1.amenity_ids, list)

    def test_inheritance(self):
        """
        Test that Place is a subclass of BaseModel.
        """
        self.assertTrue(issubclass(type(self.place1), BaseModel))

if __name__ == '__main__':
    unittest.main()
