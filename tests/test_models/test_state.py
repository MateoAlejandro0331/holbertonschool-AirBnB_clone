#!/usr/bin/python3
"""Tests for 'State' class that inherits from 'BaseModel'
with unittest module"""

import unittest
import models
from models.base_model import BaseModel
from models.state import State


class TestUser(unittest.TestCase):
    """Testing our methods of 'BaseModel' for 'State'"""

    def test_doc_module(self):
        """Testing all class documentation"""

        self.assertTrue(models.state.__doc__)
        self.assertTrue(State.__doc__)

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

    def test_type_objects_State(self):
        """Testing the 'State' public attributes"""

        Model = State()

        self.assertIsInstance(Model, State)
        self.assertIsInstance(Model.name, str)

        self.assertTrue(issubclass(State, BaseModel))

    def test_instances_of_State(self):
        """Testing the 'State' public attributes"""

        Model = State()

        self.assertTrue(hasattr(Model, "name"))


if __name__ == '__main__':
    unittest.main()
