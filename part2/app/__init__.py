#!/usr/bin/python3

from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenity
from app.api.v1.places import api as place
from app.api.v1.reviews import api as review

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
    db.init_app(app)

    # Configuration de l'API avec les différentes namespaces
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenity, path='/api/v1/amenities')
    api.add_namespace(review, path='/api/v1/reviews')
    api.add_namespace(place, path='/api/v1/places')

    return app
