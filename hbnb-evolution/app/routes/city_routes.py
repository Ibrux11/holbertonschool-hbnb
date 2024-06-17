#!/usr/bin/python3
"""Routes for City"""

from flask import Blueprint, jsonify, request, abort
from models import storage
from models.city import City

city_routes = Blueprint('city_routes', __name__)

@city_routes.route('/cities', methods=['GET'])
def get_cities():
    """Retrieve all cities"""
    cities = storage.all(City)
    return jsonify([city.to_dict() for city in cities])

@city_routes.route('/cities', methods=['POST'])
def create_city():
    """Create a new city"""
    if not request.json or 'name' not in request.json or 'country_id' not in request.json:
        abort(400)
    city = City(name=request.json['name'], country_id=request.json['country_id'])
    storage.new(city)
    storage.save()
    return jsonify(city.to_dict()), 201
