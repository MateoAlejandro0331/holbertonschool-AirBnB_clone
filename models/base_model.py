#!/usr/bin/python3
"""Base class"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Constructor method"""
    def __init__(self, *args, **kwargs):
        """Initializes the objects"""

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
            storage.new(self)

    def __str__(self):
        """Returns a string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the current date and time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation"""
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()

        return self.__dict__
