#!/usr/bin/python3
"""Routes for Amenity"""

from flask import Blueprint, jsonify, request, abort
from models import storage
from models.amenity import Amenity

amenity_routes = Blueprint('amenity_routes', __name__)

@amenity_routes.route('/amenities', methods=['GET'])
def get_amenities():
    """Retrieve all amenities"""
    amenities = storage.all(Amenity)
    return jsonify([amenity.to_dict() for amenity in amenities])

@amenity_routes.route('/amenities', methods=['POST'])
def create_amenity():
    """Create a new amenity"""
    if not request.json or 'name' not in request.json:
        abort(400)
    amenity = Amenity(name=request.json['name'])
    storage.new(amenity)
    storage.save()
    return jsonify(amenity.to_dict()), 201
