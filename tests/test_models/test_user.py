#!/usr/bin/python3
"""Tests for 'User' class with unittest module"""

import unittest
import models
import json
from models.user import User
from os.path import exists


class TestUser(unittest.TestCase):
    """Testing our functions of 'User'"""

    def test_doc_module(self):
        """Testing all class documentation"""

        self.assertTrue(models.user.__doc__)
        self.assertTrue(User.__doc__)

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

        Model = User()

        str = f"[{Model.__class__.__name__}] ({Model.id}) {Model.__dict__}"
        str2 = Model.__str__()
        self.assertEqual(str, str2)

    def test_save(self):
        """Testing the 'save' method"""

        Model = User()

        Model.save()
        self.assertTrue(exists("file.json"))
        with open("file.json") as file:
            to_load = json.load(file)
        self.assertTrue(Model.to_dict() in to_load.values())

    def test_to_dict(self):
        """Testing the 'to_dict' method"""

        Model = User()

        dict = Model.to_dict()
        self.assertEqual(Model.id, dict["id"])

    def create_attributes(self):
        """Testing 'User' class creating owns attributes"""

        pass


if __name__ == '__main__':
    unittest.main()
