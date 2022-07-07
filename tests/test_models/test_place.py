#!/usr/bin/python3
"""Tests for 'Place' class that inherits from 'BaseModel'
with unittest module"""

import unittest
import models
from models.base_model import BaseModel
from models.place import Place


class TestUser(unittest.TestCase):
    """Testing our methods of 'BaseModel' for 'Place'"""

    def test_doc_module(self):
        """Testing all class documentation"""

        self.assertTrue(models.place.__doc__)
        self.assertTrue(Place.__doc__)

    def test_is_instance(self):
        """Creating an instance of 'Place'"""

        Model = Place()
        self.assertIsInstance(Model, Place)

    def test_id(self):
        """Testing if there is a different id (uuid4)"""

        instance_0 = Place()
        instance_1 = Place()
        self.assertNotEqual(instance_0, instance_1)

    def test_str(self):
        """Testing the '__str__' method"""

        Model = Place()

        str = f"[{Model.__class__.__name__}] ({Model.id}) {Model.__dict__}"
        str2 = Model.__str__()
        self.assertEqual(str, str2)

    def test_type_objects_Place(self):
        """Testing the 'User' public attributes"""

        Model = Place()

        self.assertIsInstance(Model, Place)
        self.assertIsInstance(Model.city_id, str)
        self.assertIsInstance(Model.user_id, str)
        self.assertIsInstance(Model.name, str)
        self.assertIsInstance(Model.description, str)
        self.assertIsInstance(Model.number_rooms, int)
        self.assertIsInstance(Model.number_bathrooms, int)
        self.assertIsInstance(Model.max_guest, int)
        self.assertIsInstance(Model.price_by_night, int)
        self.assertIsInstance(Model.latitude, float)
        self.assertIsInstance(Model.latitude, float)
        self.assertIsInstance(Model.amenity_ids, list)

        self.assertTrue(issubclass(Place, BaseModel))

    def test_instances_of_Place(self):
        """Testing the 'User' public attributes"""

        Model = Place()

        self.assertTrue(hasattr(Model, "city_id"))
        self.assertTrue(hasattr(Model, "user_id"))
        self.assertTrue(hasattr(Model, "name"))
        self.assertTrue(hasattr(Model, "description"))
        self.assertTrue(hasattr(Model, "number_rooms"))
        self.assertTrue(hasattr(Model, "number_bathrooms"))
        self.assertTrue(hasattr(Model, "max_guest"))
        self.assertTrue(hasattr(Model, "price_by_night"))
        self.assertTrue(hasattr(Model, "latitude"))
        self.assertTrue(hasattr(Model, "longitude"))
        self.assertTrue(hasattr(Model, "amenity_ids"))


if __name__ == '__main__':
    unittest.main()
