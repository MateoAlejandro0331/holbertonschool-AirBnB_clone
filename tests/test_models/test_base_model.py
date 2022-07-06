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


if __name__ == '__main__':
    unittest.main()
