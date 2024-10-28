#!/usr/bin/python3

from datetime import datetime
import uuid

class Review:
    def __init__(self, title: str, text: str, rating: int, place_id: str, user_id: str):
        self.id = str(uuid.uuid4())  # Generate a unique identifier
        self.text = text
        self.title = title
        self.rating = rating
        self.place_id = place_id  # ID of the Place being reviewed
        self.user_id = user_id  # ID of the User writing the review
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        # Validate data
        self.validate()

    def validate(self):
        if not (0 <= self.rating <= 5):
            raise ValueError("Rating must be between 0 and 5.")
        if not self.text:
            raise ValueError("Review text cannot be empty.")

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.updated_at = datetime.now()
