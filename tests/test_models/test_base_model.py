#!/usr/bin/python3
"""Tests for 'BaseModel' class with unittest module"""

import json
import unittest
from models.base_model import BaseModel
from os.path import exists


class TestBaseModel(unittest.TestCase):
    """Testing our functions of 'BaseModel'"""

    def test_is_instance(self):
        """Creating an instance of 'BaseModel'"""

        Model = BaseModel()
        self.assertIsInstance(Model, BaseModel)

    def test_id(self):
        """Testing if there is a different id (uuid4)"""

        instance_0 = BaseModel()
        instance_1 = BaseModel()
        self.assertNotEqual(instance_0, instance_1)

    def test_str(self):
        """Testing the '__str__' method"""

        str = f"[{self.Model.__class__.__name__}] \
                    ({self.Model.id}) {self.Model.__dict__}"
        str2 = self.Model.__str__()
        self.assertEqual(str, str2)


if __name__ == '__main__':
    unittest.main()
