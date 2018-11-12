#!/usr/bin/python3
"""This module defines a class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines a City
    Attributes:
    place_id (string): Place.id
    user_id (string): User.id
    text (string): empty to begin with
    """
    place_id = ""
    user_id = ""
    text = ""
