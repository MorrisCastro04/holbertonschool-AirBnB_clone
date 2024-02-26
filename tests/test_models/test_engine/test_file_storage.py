#!/usr/bin/python3
import unittest
from json import dumps
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestAll(unittest.TestCase):
    """test the method all"""
    def test_no_arguments(self):
        """test without args"""
        test_instance = FileStorage()
        self.assertEqual(test_instance.all(), FileStorage._FileStorage__objects)

    def test_objects_type(self):
        """test the type of the obj"""
        test_instance = FileStorage()

        for obj in test_instance.all().values():
            self.assertIsInstance(obj, dict)

    def test_arguments(self):
        """test with args"""
        test_instance = FileStorage()
        with self.assertRaises(TypeError):
            test_instance.all("never gonna give you up")


class TestNew(unittest.TestCase):
    """test the method New"""
    def test_no_arguments(self):
        """test without args"""
        test_instance = FileStorage()
        with self.assertRaises(TypeError):
            test_instance.new()

    def test_more_arguments(self):
        """test with args"""
        test_instance = FileStorage()
        with self.assertRaises(TypeError):
            test_instance.new("I don't know", complex(float(), int()))


class TestSave(unittest.TestCase):
    """test the method save"""
    def test_no_arguments(self):
        """test without args"""
        test_instance = FileStorage()
        test_instance.save()

        with open(FileStorage._FileStorage__file_path, "r") as file:
            expected_output = dumps(test_instance.all())
            self.assertEqual(file.read(), expected_output)

    def test_arguments(self):
        """test with args"""
        test_instance = FileStorage()
        with self.assertRaises(TypeError):
            test_instance.save("hi")

class testReload(unittest.TestCase):
    """test the method reload"""
    def test_reload_correcly(self):
        """test if the  reload convert to __obj"""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        storage.reload()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, storage.all())

if __name__ == '__main__':
    unittest.main()