#!/usr/bin/python3
"""
Main 'BaseModel' class that defines all common
attributes/methods for other classes
"""

import uuid
import models
from datetime import datetime


class BaseModel:
    """ Base class constructor method """

    def __init__(self, *args, **kwargs):
        """ Base class initializes the objects """

        if kwargs:
            for key_inside, value_inside in kwargs.items():
                if key_inside != "__class__":
                    setattr(self, key_inside, value_inside)

                format = "%Y-%m-%dT%H:%M:%S.%f"
                if key_inside == "created_at":
                    value_inside = datetime.strptime(value_inside, format)

                if key_inside == "updated_at":
                    value_inside = datetime.strptime(value_inside, format)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Method that returns a string representation """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Method that update the current date and time """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Method that returns a dictionary representation """

        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict
