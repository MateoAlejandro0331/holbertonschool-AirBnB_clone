#!/usr/bin/python3
"""Tests for 'BaseModel' class with unittest module"""

import unittest
import models
import json
from models.base_model import BaseModel
from os.path import exists


class TestBaseModel(unittest.TestCase):
    """Testing our functions of 'BaseModel'"""

    @classmethod
    def setUpClass(cls):
        """Method called before tests in an individual class are run"""
        Model = BaseModel()

    def test_docs(self):
        """Testing all class documentation"""

        self.assertTrue(models.base_model.__doc__)
        self.assertTrue(BaseModel.__doc__)
        self.assertTrue(BaseModel.__init__.__doc__)
        self.assertTrue(BaseModel.__str__.__doc__)
        self.assertTrue(BaseModel.save.__doc__)
        self.assertTrue(BaseModel.to_dict.__doc__)

    def test_is_an_instance(self):
        """Creating an instance of 'BaseModel'"""

        Model = BaseModel()
        self.assertIsInstance(Model, BaseModel)

    def test_different_id(self):
        """Testing if there is a different id (uuid4)"""

        instance_0 = BaseModel()
        instance_1 = BaseModel()
        self.assertNotEqual(instance_0, instance_1)

    def test_str(self):
        """Testing the '__str__' method"""

        Model = BaseModel()

        str = f"[{Model.__class__.__name__}] ({Model.id}) {Model.__dict__}"
        str2 = Model.__str__()
        self.assertEqual(str, str2)

    def test_save(self):
        """Testing the 'save' method"""

        Model = BaseModel()

        Model.save()
        self.assertTrue(exists("file.json"))
        with open("file.json") as file:
            to_load = json.load(file)
        self.assertTrue(Model.to_dict() in to_load.values())

    def test_to_dict(self):
        """Testing the 'to_dict' method"""

        Model = BaseModel()

        dict = Model.to_dict()
        self.assertEqual(Model.id, dict["id"])

    def test_attributes(self):
        """Testing the attributes of 'BaseModel'"""

        Model = BaseModel()

        self.assertIsInstance(Model, BaseModel)
        self.assertTrue(hasattr(Model, "created_at"))
        self.assertTrue(hasattr(Model, "updated_at"))
        self.assertTrue(hasattr(Model, "id"))

    def test_attributes_dictionary(self):
        """Testing the attributes of 'BaseModel'"""

        Model = BaseModel()

        Model.name = "Matein Pingüin"
        self.assertTrue(hasattr(Model, "name"))
        self.assertEqual(Model.to_dict()["name"], "Matein Pingüin")


if __name__ == '__main__':
    unittest.main()
