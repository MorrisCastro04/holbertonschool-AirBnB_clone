#!/usr/bin/python3
"""Base Model Class"""
import uuid
from datetime import datetime


class BaseModel():
    """
    Attributes:
        id (str): The unique identifier of the instance.
        created_at (datetime): The datetime when the instance was created.
        updated_at (datetime): The datetime when the instance was last updated.
    """

    def __init__(self):
        """initializacion of the model class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of BaseModel."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Converts the object to a dictionary representation."""
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

    @classmethod
    def from_dict(cls, obj_dict):
        """Recreates an instance from a dictionary representation."""
        class_name = obj_dict.pop('__class__', None)
        if class_name is None or class_name != cls.__name__:
            raise ValueError(
                f"Invalid or missing '__class__' in dictionary: {obj_dict}")
        obj_dict['created_at'] = datetime.fromisoformat(obj_dict['created_at'])
        obj_dict['updated_at'] = datetime.fromisoformat(obj_dict['updated_at'])
        instance = cls.__new__(cls)
        instance.__dict__.update(obj_dict)
        return instance
