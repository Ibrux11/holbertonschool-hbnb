#!/usr/bin/python3

from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.persistence.repository import InMemoryRepository


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def update_user(self, user_id, user_data):
        user = self.get_user(user_id)
        if user:
            for key, value in user_data.items():
                setattr(user, key, value)
            self.user_repo.update(user, user_data)
        return user

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity(amenity_id)
        if amenity:
            for key, value in amenity_data.items():
                setattr(amenity, key, value)
            self.amenity_repo.update(amenity, amenity_data)
        return amenity

    def create_place(self, place_data):
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        if place:
            # Mettre à jour les attributs du lieu avec les nouvelles données
            for key, value in place_data.items():
                setattr(place, key, value)
            self.place_repo.update(place, place_data)
        return place

    def create_review(self, review_data):
        # Validate the presence of user_id, place_id, and rating
        user = User.query.get(review_data.get('user_id'))
        place = Place.query.get(review_data.get('place_id'))
        if not user or not place:
            raise ValueError('Invalid user_id or place_id')

        # Validate rating is between 1 and 5
        if not (1 <= review_data['rating'] <= 5):
            raise ValueError('Rating must be between 1 and 5')

        # Create and save the review
        review = Review(**review_data)
        db.session.add(review)
        db.session.commit()
        return review

    def get_review(self, review_id):
        review = Review.query.get(review_id)
        if not review:
            raise ValueError('Review not found')
        return review

    def get_all_reviews(self):
        return Review.query.all()

    def get_reviews_by_place(self, place_id):
        place = Place.query.get(place_id)
        if not place:
            raise ValueError('Place not found')
        return place.reviews

    def update_review(self, review_id, review_data):
        review = Review.query.get(review_id)
        if not review:
            raise ValueError('Review not found')

        if 'rating' in review_data and not (1 <= review_data['rating'] <= 5):
            raise ValueError('Rating must be between 1 and 5')

        for key, value in review_data.items():
            setattr(review, key, value)
        db.session.commit()
        return review

    def delete_review(self, review_id):
        review = Review.query.get(review_id)
        if not review:
            raise ValueError('Review not found')
        db.session.delete(review)
        db.session.commit()
