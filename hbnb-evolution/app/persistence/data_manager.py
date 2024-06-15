#!/user/bin/python3
import json
import os
class DataManager:
    def __init__(self, storage_file):
        self.storage_file = storage_file
        self.data = self._load_data()

    def _load_data(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                return json.load(file)
        else:
            return {'users': {}, 'listings': {}}

    def _save_data(self):
        with open(self.storage_file, 'w') as file:
            json.dump(self.data, file, indent=4)

    def save(self, entity):
        entity_type = type(entity).__name__.lower()
        entity_id = entity.get('id')
        if entity_type not in self.data:
            self.data[entity_type] = {}
        self.data[entity_type][entity_id] = entity
        self._save_data()

    def get(self, entity_id, entity_type):
        if entity_type in self.data:
            return self.data[entity_type].get(entity_id)
        return None

    def update(self, entity):
        entity_type = type(entity).__name__.lower()
        entity_id = entity.get('id')
        if entity_type in self.data and entity_id in self.data[entity_type]:
            self.data[entity_type][entity_id] = entity
            self._save_data()

    def delete(self, entity_id, entity_type):
        if entity_type in self.data and entity_id in self.data[entity_type]:
            del self.data[entity_type][entity_id]
            self._save_data()

class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

class Listing:
    def __init__(self, id, title, description, owner_id):
        self.id = id
        self.title = title
        self.description = description
        self.owner_id = owner_id

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'owner_id': self.owner_id
        }

class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

class Listing:
    def __init__(self, id, title, description, owner_id):
        self.id = id
        self.title = title
        self.description = description
        self.owner_id = owner_id

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'owner_id': self.owner_id
        }

if __name__ == "__main__":
    storage_file = 'data.json'
    data_manager = DataManager(storage_file)

    user = User(1, 'john_doe', 'john@example.com').to_dict()
    data_manager.save(user)

    listing = Listing(1, 'Cozy Apartment', 'A nice place to stay.', 1).to_dict()
    data_manager.save(listing)

    retrieved_user = data_manager.get(1, 'users')
    print(retrieved_user)

    retrieved_listing = data_manager.get(1, 'listings')
    print(retrieved_listing)

    user['email'] = 'john.doe@example.com'
    data_manager.update(user)

    data_manager.delete(1, 'listings')
