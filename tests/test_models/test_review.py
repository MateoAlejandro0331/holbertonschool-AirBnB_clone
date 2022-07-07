#!/usr/bin/python3
"""Tests for 'Review' class that inherits from 'BaseModel'
with unittest module"""

import unittest
import models
from models.base_model import BaseModel
from models.review import Review


class TestUser(unittest.TestCase):
    """Testing our methods of 'BaseModel' for 'Review'"""

    def test_doc_module(self):
        """Testing all class documentation"""

        self.assertTrue(models.review.__doc__)
        self.assertTrue(Review.__doc__)

    def test_is_instance(self):
        """Creating an instance of 'Review'"""

        Model = Review()
        self.assertIsInstance(Model, Review)

    def test_id(self):
        """Testing if there is a different id (uuid4)"""

        instance_0 = Review()
        instance_1 = Review()
        self.assertNotEqual(instance_0, instance_1)

    def test_str(self):
        """Testing the '__str__' method"""

        Model = Review()

        str = f"[{Model.__class__.__name__}] ({Model.id}) {Model.__dict__}"
        str2 = Model.__str__()
        self.assertEqual(str, str2)

    def test_type_objects_Review(self):
        """Testing the 'Amenity' public attributes"""

        Model = Review()

        self.assertIsInstance(Model, Review)
        self.assertIsInstance(Model.place_id, str)
        self.assertIsInstance(Model.user_id, str)
        self.assertIsInstance(Model.text, str)

        self.assertTrue(issubclass(Review, BaseModel))

    def test_instances_of_Amenity(self):
        """Testing the 'Amenity' public attributes"""

        Model = Review()

        self.assertTrue(hasattr(Model, "place_id"))
        self.assertTrue(hasattr(Model, "user_id"))
        self.assertTrue(hasattr(Model, "text"))


if __name__ == '__main__':
    unittest.main()
