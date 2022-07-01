#!/usr/bin/python3
"""Base class"""

import uuid
import datetime


class BaseModel:
    """Constructor method"""
    def __init__(self, *args, **kwargs):
        """Initializes the objects"""

        if kwargs:
            for key, value in kwargs.items():
                if key or value is "__class__":
                    pass

                if key is "created_at" or key is "updated_at":
                    datetime_format = "%Y-%m-%dT%H:%M:%S.%f"
                    value = datetime.datetime.strptime(value, datetime_format)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns a string representation"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the current date and time"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary representation"""
        new_dict = dict(self.__dict__)
        new_dict.update(__class__=__class__.__name__)
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict
