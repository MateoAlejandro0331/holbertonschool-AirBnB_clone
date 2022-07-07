#!/usr/bin/python3
"""Tests for 'User' class with unittest module"""

import unittest

from attr import has
import models
import json
from models.base_model import BaseModel
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

    def test_instances_of_User(self):
        """Testing the 'User' public attributes"""

        Model = User()

        self.assertTrue(hasattr(Model, "email"))
        self.assertTrue(hasattr(Model, "password"))
        self.assertTrue(hasattr(Model, "first_name"))
        self.assertTrue(hasattr(Model, "last_name"))

    def test_type_objects_User(self):
        """Testing type of 'User' attributes (objects)"""

        Model = User()

        self.assertIsInstance(Model.email, str)
        self.assertIsInstance(Model.password, str)
        self.assertIsInstance(Model.first_name, str)
        self.assertIsInstance(Model.last_name, str)

        self.assertTrue(issubclass(User, BaseModel))


if __name__ == '__main__':
    unittest.main()
