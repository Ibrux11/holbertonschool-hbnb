#!/usr/bin/python3
import uuid
from datetime import datetime
from user import User


class Place:
    def __init__(self, title: str, price: float, latitude: float, longitude: float, owner: User, description: str = ""):
        self.id = str(uuid.uuid4())  # Generate a unique identifier
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner  # User instance
        self.created_at = datetime.now()  # Timestamp for creation
        self.updated_at = datetime.now()  # Timestamp for updates
        # Will hold a list of Amenity instances (many-to-many relationship)
        self.amenities = []
        # Will hold a list of Review instances (one-to-many relationship)
        self.reviews = []

        # Validation
        self.validate()

    def validate(self):
        if len(self.title) > 100:
            raise ValueError("Title must not exceed 100 characters.")
        if self.price <= 0:
            raise ValueError("Price must be a positive value.")
        if not (-90.0 <= self.latitude <= 90.0):
            raise ValueError("Latitude must be between -90.0 and 90.0.")
        if not (-180.0 <= self.longitude <= 180.0):
            raise ValueError("Longitude must be between -180.0 and 180.0.")

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.updated_at = datetime.now()  # Update timestamp

    def add_review(self, review: 'Review'):  # Use a string to reference the 'Review' type
        """Ajoute une review."""
        self.reviews.append(review)
        self.updated_at = datetime.now()  # Update timestamp whenever a new review is added

    # Validation for price, latitude, and longitude

    @property
    def price(self):
        # Getter for the price attribute
        return self._price

    @price.setter
    def price(self, value):
        # Setter for price with validation
        # Ensures price is non-negative, raises ValueError if invalid
        if value < 0:
            raise ValueError("Price must be a non-negative number")
        self._price = value

    @property
    def latitude(self):
        # Getter for the latitude attribute
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        # Setter for latitude with validation
        # Ensures latitude is between -90 and 90, raises ValueError if invalid
        if not (-90 <= value <= 90):
            raise ValueError("Latitude must be between -90 and 90")
        self._latitude = value

    @property
    def longitude(self):
        # Getter for the longitude attribute
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        # Setter for longitude with validation
        # Ensures longitude is between -180 and 180, raises ValueError if invalid
        if not (-180 <= value <= 180):
            raise ValueError("Longitude must be between -180 and 180")
        self._longitude = value
