#!/usr/bin/python3
"""Tests for 'Review' class that inherits from 'BaseModel'
with unittest module"""

import unittest
from models.review import Review


class TestUser(unittest.TestCase):
    """Testing our methods of 'BaseModel' for 'Review'"""

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

        str = f"[{self.Model.__class__.__name__}] \
                    ({self.Model.id}) {self.Model.__dict__}"
        str2 = self.Model.__str__()
        self.assertEqual(str, str2)


if __name__ == '__main__':
    unittest.main()
