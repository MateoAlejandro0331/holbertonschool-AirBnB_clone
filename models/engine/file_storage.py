#!/usr/bin/python3
"""Class to store the objects"""

import json
from os.path import exists
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel


class FileStorage:
    """Serializes and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    clss_0 = {"BaseModel": BaseModel, "Amenity": Amenity, "User": User}
    clss_1 = {"State": State, "City": City, "Review": Review, "Place": Place}

    classes = clss_0.update(clss_1)

    def all(self):
        """Returns the dictionary '__objects'"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in '__objects' the obj with key '<obj class name>.id'"""
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes '__objects' to the JSON file '(path: __file_path)'"""

        dict_to_serialize = {}

        for key_inside, value_inside in FileStorage.__objects.items():
            dict_to_serialize[key_inside] = value_inside.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(dict_to_serialize, file)

        """with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            Obj = json.dumps(FileStorage.__objects,
            sort_keys=True, default=str)
            file.write(Obj)"""

    def reload(self):
        """Deserializes the JSON file to __objects"""

        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                for key, value in json.load(file).items():
                    Obj = FileStorage.__objects
                    Obj[key] = FileStorage.classes[value["__class__"]](**value)
