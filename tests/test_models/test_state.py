#!/usr/bin/python3
"""Tests for 'State' class that inherits from 'BaseModel'
with unittest module"""

import unittest
from models.state import State


class TestUser(unittest.TestCase):
    """Testing our methods of 'BaseModel' for 'State'"""

    def test_is_instance(self):
        """Creating an instance of 'State'"""

        Model = State()
        self.assertIsInstance(Model, State)

    def test_id(self):
        """Testing if there is a different id (uuid4)"""

        instance_0 = State()
        instance_1 = State()
        self.assertNotEqual(instance_0, instance_1)

    def test_str(self):
        """Testing the '__str__' method"""

        Model = State()

        str = f"[{Model.__class__.__name__}] ({Model.id}) {Model.__dict__}"
        str2 = Model.__str__()
        self.assertEqual(str, str2)


if __name__ == '__main__':
    unittest.main()
