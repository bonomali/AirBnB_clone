#!/usr/bin/python3
"""This module defines a class City"""

from models.base_model import BaseModel


class City(BaseModel):
    """This class defines a City
    Attributes:
    state_id (string): State.id
    name (string): State name
    """
    state_id = ""
    name = ""
