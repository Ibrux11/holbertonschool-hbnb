#!/usr/bin/python3
"""Main module for registering routes"""

from flask import Flask
from amenity_routes import amenity_routes
from city_routes import city_routes
from country_routes import country_routes
from place_routes import place_routes
from review_routes import review_routes
from user_routes import user_routes

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(amenity_routes, url_prefix='/api/v1')
app.register_blueprint(city_routes, url_prefix='/api/v1')
app.register_blueprint(country_routes, url_prefix='/api/v1')
app.register_blueprint(place_routes, url_prefix='/api/v1')
app.register_blueprint(review_routes, url_prefix='/api/v1')
app.register_blueprint(user_routes, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
