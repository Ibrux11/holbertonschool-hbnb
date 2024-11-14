#!/usr/bin/python3

import uuid
from datetime import datetime
from app.models.user import User

class Place:
    def __init__(self, title, price, latitude, longitude, user, amenities, description=""):
        self.id = str(uuid.uuid4())  # ID unique
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.user = user
        self.amenities = amenities
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.validate()

    def validate(self):
        if not 0 <= self.price:
            raise ValueError("Price must be a positive number.")
        if not -90 <= self.latitude <= 90:
            raise ValueError("Latitude must be between -90 and 90.")
        if not -180 <= self.longitude <= 180:
            raise ValueError("Longitude must be between -180 and 180.")

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.updated_at = datetime.now()
