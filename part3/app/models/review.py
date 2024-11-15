#!/usr/bin/python3
from extensions import db
from datetime import datetime
from .baseclass import BaseModel


class Review(BaseModel):
    __tablename__ = 'reviews'

    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    # Foreign Key to Place (One-to-Many)
    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)

    # Foreign Key to User (One-to-Many)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)

    # Relationship with Place (One-to-Many)
    place = db.relationship('Place', back_populates='reviews')

    # Relationship with User (One-to-Many)
    user = db.relationship('User', back_populates='reviews')
