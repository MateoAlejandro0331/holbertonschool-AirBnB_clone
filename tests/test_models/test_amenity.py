#!/usr/bin/python3
"""Tests for 'Amenity' class that inherits from 'BaseModel'
with unittest module"""

import unittest
from models.amenity import Amenity


class TestUser(unittest.TestCase):
    """Testing our methods of 'BaseModel' for 'Amenity'"""

    def test_is_instance(self):
        """Creating an instance of 'Amenity'"""

        Model = Amenity()
        self.assertIsInstance(Model, Amenity)

    def test_id(self):
        """Testing if there is a different id (uuid4)"""

        instance_0 = Amenity()
        instance_1 = Amenity()
        self.assertNotEqual(instance_0, instance_1)

    def test_str(self):
        """Testing the '__str__' method"""

        Model = Amenity()

        str = f"[{Model.__class__.__name__}] ({Model.id}) {Model.__dict__}"
        str2 = Model.__str__()
        self.assertEqual(str, str2)


if __name__ == '__main__':
    unittest.main()
