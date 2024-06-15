#!/usr/bin/python3
"""Module for user"""

import models
from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel


class User(BaseModel):
    """Class representing a user.

    Attributes:
        email (str): User's email address.
        password (str): User's password.
        first_name (str): User's first name.
        last_name (str): User's last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""