#!/usr/bin/python3
"""
Instantiating BaseModel.
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Testing our function
    """

    def is_instance(self):
        """
        Create instance BaseModel
        """
        my_BaseModel = BaseModel()
        self.assertIsInstance(my_BaseModel, BaseModel)

    def test_id(self):
        """
        Check if there is a different Id
        """
        instance_0 = BaseModel()
        instance_1 = BaseModel()
        self.assertNotEqual(instance_0, instance_1)


if __name__ == '__main__':
    unittest.main()
