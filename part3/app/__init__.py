# app/__init__.py
from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenity
from app.api.v1.places import api as place
from app.api.v1.reviews import api as review
from config import DevelopmentConfig
from extensions import db, bcrypt  # Import from extensions

def create_app(config=DevelopmentConfig):
    # Instantiate the app with the provided or default configuration
    app = Flask(__name__)
    app.config.from_object(config)  # Load configuration object

    # Initialize the database and bcrypt with the application
    db.init_app(app)
    bcrypt.init_app(app)

    # Setup the API with namespaces
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenity, path='/api/v1/amenities')
    api.add_namespace(review, path='/api/v1/reviews')
    api.add_namespace(place, path='/api/v1/places')
    
    return app
