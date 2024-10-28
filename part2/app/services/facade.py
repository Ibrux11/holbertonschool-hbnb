#!/usr/bin/python3

from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    _instance = None  # Class-level variable to hold the singleton instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(HBnBFacade, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):  # Check if already initialized
            self.user_repo = InMemoryRepository()
            self.amenity_repo = InMemoryRepository()
            self.place_repo = InMemoryRepository()
            self.review_repo = InMemoryRepository()
            self.initialized = True  # Set a flag indicating initialization

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
        # Validation pour vérifier que le owner_id est un utilisateur valide
        user = self.get_user(place_data['owner_id'])
        if not user:
            raise ValueError("Invalid owner_id; user does not exist.")

        # Création de l'objet Place
        place = Place(
            title=place_data['title'],
            description=place_data.get('description', ''),
            price=place_data['price'],
            latitude=place_data['latitude'],
            longitude=place_data['longitude'],
            user=user,
            amenities=place_data.get('amenities', [])
        )

        # Enregistrement de la Place dans le dépôt
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)
    
    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        if place:
            for key, value in place_data.items():
                setattr(place, key, value)
            self.place_repo.update(place, place_data)
        return place

    def create_review(self, review_data):
        user_id = review_data.get('user_id')
        user = self.get_user(user_id)
        place_id = review_data.get('place_id')
        place = self.get_place(place_id)
        if not user:
            raise ValueError("Invalid user ID")
        if not place:
            raise ValueError("Invalid place ID")
        review = Review(
            title=review_data.get('title', ""),
            text=review_data['text'],
            rating=review_data['rating'],
            place_id=place_id,
            user_id=user_id
        )
        self.review_repo.add(review)
        return review
    
    def get_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError("Review not found")
        return review

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        return [review for review in self.review_repo.get_all() if review.place_id == place_id]

    def update_review(self, review_id, review_data):
        review = self.get_review(review_id)
        if not review:
            raise ValueError("Review not found")
        review.update(**review_data)  # Update the review object
        self.review_repo.update(review.id, review_data)  # Update in the repository
        return review

    def delete_review(self, review_id):
        if not self.review_repo.get(review_id):
            raise ValueError("Review not found")
        self.review_repo.delete(review_id)
        return True

# Create a single global instance of the HBnBFacade
facade = HBnBFacade()
