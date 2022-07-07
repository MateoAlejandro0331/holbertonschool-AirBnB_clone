#!/usr/bin/python3
"""Tests for 'Amenity' class that inherits from 'BaseModel'
with unittest module"""

import unittest
import models
from models.amenity import Amenity
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Testing our methods of 'BaseModel' for 'Amenity'"""

    def test_doc_module(self):
        """Testing all class documentation"""

        self.assertTrue(models.amenity.__doc__)
        self.assertTrue(Amenity.__doc__)

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

    def test_type_objects_Amenity(self):
        """Testing the 'Amenity' public attributes"""

        Model = Amenity()

        self.assertIsInstance(Model, Amenity)
        self.assertIsInstance(Model.name, str)

        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_instances_of_Amenity(self):
        """Testing the 'Amenity' public attributes"""

        Model = Amenity()

        self.assertTrue(hasattr(Model, "name"))


if __name__ == '__main__':
    unittest.main()
