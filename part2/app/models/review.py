#!/usr/bin/python3
import uuid
from datetime import datetime
from user import User

class Review:
    def __init__(self, text: str, rating: int, place: 'Place', user: User):  # Use a string to reference 'Place' type
        self.id = str(uuid.uuid4())  # Generate a unique identifier
        self.text = text
        self.rating = rating
        self.place = place  # Place instance being reviewed
        self.user = user  # User instance writing the review
        self.created_at = datetime.now()  # Timestamp for creation
        self.updated_at = datetime.now()  # Timestamp for updates

        # Validation
        self.validate()

    def validate(self):
        if not (1 <= self.rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        if not self.text:
            raise ValueError("Review text cannot be empty.")

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.updated_at = datetime.now()  # Update timestamp
