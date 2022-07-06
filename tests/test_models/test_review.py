#!/usr/bin/python3
"""Tests for 'Review' class that inherits from 'BaseModel'
with unittest module"""

import unittest
import models
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


if __name__ == '__main__':
    unittest.main()
