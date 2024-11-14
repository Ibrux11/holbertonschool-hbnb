#!/usr/bin/python3
import uuid
from datetime import datetime

class Amenity:
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())  # Generate a unique identifier
        self.name = name
        self.created_at = datetime.now()  # Timestamp for creation
        self.updated_at = datetime.now()  # Timestamp for updates

        # Validation
        self.validate()

    def validate(self):
        if len(self.name) > 50:
            raise ValueError("Amenity name must not exceed 50 characters.")

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.updated_at = datetime.now()  # Update timestamp
