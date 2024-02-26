#!/usr/bin/python3
import unittest
from json import dumps
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestAll(unittest.TestCase):
    def test_no_arguments(self):
        test_instance = FileStorage()
        self.assertEqual(test_instance.all(), FileStorage._FileStorage__objects)
    
    def test_objects_type(self):
        test_instance = FileStorage()

        for obj in test_instance.all().values():
            self.assertIsInstance(obj, dict)

    def test_arguments(self):
        test_instance = FileStorage()
        with self.assertRaises(TypeError):
            test_instance.all("never gonna give you up")


class TestNew(unittest.TestCase):
    def test_no_arguments(self):
        test_instance = FileStorage()
        with self.assertRaises(TypeError):
            test_instance.new()

    def test_more_arguments(self):
        test_instance = FileStorage()
        with self.assertRaises(TypeError):
            test_instance.new("I don't know", complex(float(), int()))


class TestSave(unittest.TestCase):
    def test_no_arguments(self):
        test_instance = FileStorage()
        test_instance.save()

        with open(FileStorage._FileStorage__file_path, "r") as file:
            expected_output = dumps(test_instance.all())
            self.assertEqual(file.read(), expected_output)

    def test_arguments(self):
        test_instance = FileStorage()
        with self.assertRaises(TypeError):
            test_instance.save("hi")