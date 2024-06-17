#!/usr/bin/python3
"""Routes for Place"""

from flask import Blueprint, jsonify, request, abort
from models import storage
from models.place import Place

place_routes = Blueprint('place_routes', __name__)

@place_routes.route('/places', methods=['GET'])
def get_places():
    """Retrieve all places"""
    places = storage.all(Place)
    return jsonify([place.to_dict() for place in places])

@place_routes.route('/places', methods=['POST'])
def create_place():
    """Create a new place"""
    if not request.json:
        abort(400)
    place = Place(
        city_id=request.json.get('city_id', ""),
        user_id=request.json.get('user_id', ""),
        name=request.json.get('name', ""),
        description=request.json.get('description', ""),
        number_rooms=request.json.get('number_rooms', 0),
        number_bathrooms=request.json.get('number_bathrooms', 0),
        max_guest=request.json.get('max_guest', 0),
        price_by_night=request.json.get('price_by_night', 0),
        latitude=request.json.get('latitude', 0.0),
        longitude=request.json.get('longitude', 0.0),
        amenity_ids=request.json.get('amenity_ids', [])
    )
    storage.new(place)
    storage.save()
    return jsonify(place.to_dict()), 201

