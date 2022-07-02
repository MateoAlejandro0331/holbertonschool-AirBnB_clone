#!/usr/bin/python3
"""Class to store the objects"""

import json
from os.path import exists


class FileStorage:
    """Serializes and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary '__objects'"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in '__objects' the obj with key '<obj class name>.id'"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes '__objects' to the JSON file '(path: __file_path)'"""

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            Fs_Ob = FileStorage.__objects
            Fs_Ob = json.dumps(Fs_Ob, sort_keys=True, default=str)
            file.write(Fs_Ob)

    def reload(self):
        """Deserializes the JSON file to __objects"""

        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                FileStorage.__objects = json.loads(file.read())
