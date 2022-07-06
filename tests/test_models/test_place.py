#!/usr/bin/python3
"""Tests for 'Place' class that inherits from 'BaseModel'
with unittest module"""

import unittest
from models.place import Place


class TestUser(unittest.TestCase):
    """Testing our methods of 'BaseModel' for 'Place'"""

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

        str = f"[{self.Model.__class__.__name__}] \
                    ({self.Model.id}) {self.Model.__dict__}"
        str2 = self.Model.__str__()
        self.assertEqual(str, str2)


if __name__ == '__main__':
    unittest.main()
