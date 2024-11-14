#!/usr/bin/python3

import uuid
from datetime import datetime
from extensions import bcrypt
from extensions import db, bcrypt
from .base_model import BaseModel

class User:
    def __init__(self, first_name: str, last_name: str, email: str, password: str, is_admin: bool = False):
        self.id = str(uuid.uuid4())  # Generate a unique identifier
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.created_at = datetime.now()  # Timestamp for creation
        self.updated_at = datetime.now()  # Timestamp for updates

        # Validation
        self.validate()

    def validate(self):
        if len(self.first_name) > 50 or len(self.last_name) > 50:
            raise ValueError("First and last name must not exceed 50 characters.")
        if "@" not in self.email or "." not in self.email:
            raise ValueError("Invalid email format.")

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.updated_at = datetime.now()  # Update timestamp whenever the user object is modified

    @staticmethod
    def hash_password(password):
        """Hashes the password before storing it."""
        return bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)
    
class BaseModel(db.Model):
    __abstract__ = True  # Assure que SQLAlchemy ne crée pas de table pour BaseModel

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
class User(BaseModel):
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def hash_password(self, password):
        """Hache le mot de passe avant de le stocker."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Vérifie le mot de passe haché."""
        return bcrypt.check_password_hash(self.password, password)