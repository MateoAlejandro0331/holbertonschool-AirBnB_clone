#!/usr/bin/python3
"""Tests for 'FileStorage' class with unittest module"""

import unittest
import models
import json
from os.path import exists
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Testing our functions of 'FileStorage'"""

    @classmethod
    def setUpClass(cls):
        """Method called before tests in an individual class are run"""
        Model = FileStorage()

    def test_doc_module(self):
        """Testing all class documentation"""

        self.assertTrue(models.engine.file_storage.__doc__)
        self.assertTrue(FileStorage.__doc__)
        self.assertTrue(FileStorage.all.__doc__)
        self.assertTrue(FileStorage.new.__doc__)
        self.assertTrue(FileStorage.save.__doc__)
        self.assertTrue(FileStorage.reload.__doc__)

    def test_is_instance(self):
        """Creating an instance of 'FileStorage'"""

        Model = FileStorage()
        self.assertIsInstance(Model, FileStorage)

    def test_id(self):
        """Testing if there is a different id (uuid4)"""

        instance_0 = FileStorage()
        instance_1 = FileStorage()
        self.assertNotEqual(instance_0, instance_1)

    def test_save(self):
        """Testing the 'save' method"""

        Model = BaseModel()

        Model.save()
        self.assertTrue(exists("file.json"))
        with open("file.json") as file:
            to_load = json.load(file)
        self.assertTrue(Model.to_dict() in to_load.values())

    def test_reload(self):
        """Testing the 'reload' method"""

        Model = FileStorage()

        Model.save()
        Model.reload()
        self.assertIsInstance(Model._FileStorage__objects, dict)
        self.assertIsInstance(Model._FileStorage__objects
                              [BaseModel.__class__.__name__ + '.'
                               + BaseModel.id], BaseModel)

    def test_all(self):
        """Testing the 'all' method"""

        Model = FileStorage()

        returned_dict = Model.all()
        self.assertIsNotNone(returned_dict)
        self.assertIs(returned_dict, Model._FileStorage__objects)
        self.assertTrue(type(returned_dict), dict)

    def test_new(self):
        """Testing the 'new' method"""

        Model = BaseModel()

        models.storage.new(Model)
        dict = models.storage.all()

        key_inside = f"{type(Model).__name__}.{Model.id}"
        all_keys = dict.keys()
        self.assertIn(key_inside, all_keys)
        self.assertEqual(dict[key_inside], Model)

    def test_type_objects(self):
        """Testing type of FileStorage attributes (objects)"""

        Model = FileStorage()

        self.assertIsInstance(Model._FileStorage__file_path, str)
        self.assertIsInstance(Model._FileStorage__objects, dict)


if __name__ == '__main__':
    unittest.main()
