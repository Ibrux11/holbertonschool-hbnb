# app/__init__.py
from config import os
from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenity
from app.api.v1.places import api as place
from app.api.v1.reviews import api as review
from app.api.v1.auth import api as auth
from config import DevelopmentConfig
from extensions import db, bcrypt, jwt  # Import from extensions

def create_app(config=DevelopmentConfig):
    # Instantiate the app with the provided or default configuration
    app = Flask(__name__)
    app.config.from_object(config)  # Load configuration object

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_default_flask_secret_key')

    # Initialize the database and bcrypt with the application
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Setup the API with namespaces
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenity, path='/api/v1/amenities')
    api.add_namespace(review, path='/api/v1/reviews')
    api.add_namespace(place, path='/api/v1/places')
    api.add_namespace(auth, path='/api/v1/auth')
    
    return app
