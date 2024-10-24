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
        self.amenities = []  # Will hold a list of Amenity instances (many-to-many relationship)
        self.reviews = []  # Will hold a list of Review instances (one-to-many relationship)

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

    # Validation du prix, de la latitude et de la longitude
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Le prix doit être un nombre non négatif")
        self._price = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if not (-90 <= value <= 90):
            raise ValueError("La latitude doit être comprise entre -90 et 90")
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not (-180 <= value <= 180):
            raise ValueError("La longitude doit être comprise entre -180 et 180")
        self._longitude = value
