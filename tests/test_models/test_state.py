#1/usr/bin/python3
"""unittest of the State Class"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def test_state_attributes(self):
        """
        Test case to verify the attributes of the State instance.
        """
        state = State()
        self.assertEqual(state.name, "")

    def test_state_inheritance(self):
        """
        Test case to verify the inheritance of the State class.
        """
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_state_init(self):
        """
        Test case to verify the initialization of the State instance.
        """
        state = State(id="123", created_at="2022-01-01T00:00:00", updated_at="2022-01-01T00:00:00")
        self.assertEqual(state.id, "123")
        self.assertEqual(state.created_at, "2022-01-01T00:00:00")
        self.assertEqual(state.updated_at, "2022-01-01T00:00:00")

if __name__ == '__main__':
    unittest.main()
