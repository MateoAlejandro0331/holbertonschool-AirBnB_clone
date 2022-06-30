#!/usr/bin/python3
"""Base class"""

from hashlib import new
import uuid
import datetime


class BaseModel:
    """Constructor method"""
    def __init__(self):
        """Initializes the objects"""
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
