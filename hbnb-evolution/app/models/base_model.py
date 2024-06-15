#!/usr/bin/python3
"""Module for BaseModel"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of the BaseModel class.

        If kwargs is not empty, set each key-value pair
            as an attribute of the instance,
        except for '__class__' which should
            not be set as an attribute.
        Specifically, convert 'created_at' and 'updated_at'
            from strings to datetime objects
        if they are present in kwargs.

        If kwargs is empty, generate a new unique ID
            and set both 'created_at' and
        'updated_at' to the current datetime.

        Parameters:
            *args (tuple): Variable length argument list,
                not used in this function.
            **kwargs (dict): Keyword arguments containing initial
                attribute names and values.

        Attributes:
            id (str): Unique identifier for the instance,
                generated using uuid4.
            created_at (datetime): Timestamp representing
                the creation time of the instance.
            updated_at (datetime): Timestamp representing the time
                of the last update of the instance.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) > 0:
            for key, valu in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        valu = datetime.strptime(valu, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, valu)
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        class_name = self.__class__.__name__
        return (f"[{class_name}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        Updates the 'updated_at' attribute with the current timestamp.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary representation.
        Adds '__class__', 'created_at', and 'updated_at' keys.
        Returns the dictionary.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict