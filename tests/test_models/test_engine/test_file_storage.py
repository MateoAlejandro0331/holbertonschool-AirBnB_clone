#!/usr/bin/python3
"""Tests for 'FileStorage' class with unittest module"""

import unittest
import models
import json
from os.path import exists
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Testing our functions of 'FileStorage'"""

    @classmethod
    def setUpClass(cls):
        """Method called before tests in an individual class are run"""
        Model = FileStorage()

    def test_doc_module(self):
        """Testing all class documentation"""

        self.assertTrue(models.engine.FileStorage.__doc__)
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


if __name__ == '__main__':
    unittest.main()
