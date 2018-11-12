#!/usr/bin/python3
"""This module defines a class User"""

from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a User
    Attributes:
    email (string): User's email
    password (string): User's password
    first_name (string): User's first name
    last_name (string): User's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
