#!/usr/bin/python3
"""unittest for the class BaseModel"""
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime


class TestModel(unittest.TestCase):
    """This class contains unit tests for the BaseModel class."""
    def test_Class(self):
        """Test the initialization of the BaseModel class."""
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))
        self.assertEqual(model.created_at, model.updated_at)

    def test_diferent_id(self):
        """Test that different instances of BaseModel have different ids."""
        model_1 = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model_1.id, model_2.id)

    def test_str(self):
        """Test the __str__ method of BaseModel."""
        model = BaseModel()
        The_str = f"[{model.__class__.__name__}] ({model.id}) {model.__dict__}"
        self.assertEqual(model.__str__(), The_str)

    def test_double_check_id_not_save(self):
        """Test that the updated not change if is call more than twice."""
        model = BaseModel()
        time_1 = model.updated_at
        time_2 = model.updated_at
        self.assertEqual(time_1, time_2)

    def test_save(self):
        """Test the save method of BaseModel."""
        model = BaseModel()
        time_1 = model.updated_at
        model.my_number = 89
        model.save()
        time_2 = model.updated_at
        self.assertNotEqual(time_1, time_2)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertTrue(isinstance(model_dict, dict))
        self.assertTrue(isinstance(model, BaseModel))


if __name__ == '__main__':
    unittest.main()
