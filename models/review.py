#!/usr/bin/python3
"""Class 'Review' that inherits from 'BaseModel'"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Public class attributes"""

    place_id = ""
    user_id = ""
    text = ""
