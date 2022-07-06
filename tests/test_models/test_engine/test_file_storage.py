#!/usr/bin/python3
"""Tests for 'FileStorage' class with unittest module"""

import unittest
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Testing our functions of 'FileStorage'"""

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


if __name__ == '__main__':
    unittest.main()
