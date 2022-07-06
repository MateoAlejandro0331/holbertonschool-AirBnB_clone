#!/usr/bin/python3
"""Tests for 'User' class with unittest module"""

import json
import unittest
from os.path import exists
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

    def test_save(self):
        """Testing the 'save' method"""

        self.Model.save()
        self.assertTrue(exists("file.json"))
        with open("file.json") as file:
            to_load = json.load(file)
        self.assertTrue(self.Model.to_dict() in to_load.values())

    def test_to_dict(self):
        """Testing the 'to_dict' method"""

        dict = self.Model.to_dict()
        self.assertEqual(self.Model.id, dict["id"])


if __name__ == '__main__':
    unittest.main()
