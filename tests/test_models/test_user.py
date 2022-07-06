#!/usr/bin/python3
"""Tests for 'User' class with unittest module"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Testing our functions of 'User'"""

    def test_is_instance(self):
        """Creating an instance of 'User'"""

        Model = User()
        self.assertIsInstance(Model, User)

    def test_id(self):
        """Testing if there is a different id (uuid4)"""

        instance_0 = User()
        instance_1 = User()
        self.assertNotEqual(instance_0, instance_1)

    def test_str(self):
        """Testing the '__str__' method"""

        str = f"[{self.Model.__class__.__name__}] \
                    ({self.Model.id}) {self.Model.__dict__}"
        str2 = self.Model.__str__()
        self.assertEqual(str, str2)


if __name__ == '__main__':
    unittest.main()
