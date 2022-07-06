#!/usr/bin/python3
"""Tests for 'City' class that inherits from 'BaseModel'
with unittest module"""

import unittest
import models
from models.city import City


class TestUser(unittest.TestCase):
    """Testing our methods of 'BaseModel' for 'City'"""

    def test_is_instance(self):
        """Creating an instance of 'City'"""

        Model = City()
        self.assertIsInstance(Model, City)

    def test_doc_module(self):
        """Testing all class documentation"""

        self.assertTrue(models.city.__doc__)
        self.assertTrue(City.__doc__)

    def test_id(self):
        """Testing if there is a different id (uuid4)"""

        instance_0 = City()
        instance_1 = City()
        self.assertNotEqual(instance_0, instance_1)

    def test_str(self):
        """Testing the '__str__' method"""

        Model = City()

        str = f"[{Model.__class__.__name__}] ({Model.id}) {Model.__dict__}"
        str2 = Model.__str__()
        self.assertEqual(str, str2)


if __name__ == '__main__':
    unittest.main()
