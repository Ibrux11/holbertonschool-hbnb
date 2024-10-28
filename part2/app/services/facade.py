#!/usr/bin/python3

from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from app.persistence.repository import InMemoryRepository


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

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

    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        if place:
            for key, value in place_data.items():
                setattr(place, key, value)
            self.place_repo.update(place, place_data)
        return place
