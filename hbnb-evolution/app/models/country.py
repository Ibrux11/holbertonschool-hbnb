#!/usr/bin/python3
"""Module for Country class"""

from models.base_model import BaseModel


class Country(BaseModel):
    """Country class that inherits from BaseModel"""

    def __init__(self, name, code, *args, **kwargs):
        """
        Initializes the class Country with the following parameters:
        :param name: str - Name of the Country.
        :param code: str - The Country international code.
        """
        super().__init__(*args, **kwargs)
        self.name = name
        self.code = code

    def to_dict(self):
        """
        Converts the Country instance to a dictionary representation.
        """
        result = super().to_dict()
        result.update({
            "name": self.name,
            "code": self.code,
        })
        return result
