#!/usr/bin/python3
"""Routes for Country"""

from flask import Blueprint, jsonify, request, abort
from models import storage
from models.country import Country

country_routes = Blueprint('country_routes', __name__)

@country_routes.route('/countries', methods=['GET'])
def get_countries():
    """Retrieve all countries"""
    countries = storage.all(Country)
    return jsonify([country.to_dict() for country in countries])

@country_routes.route('/countries', methods=['POST'])
def create_country():
    """Create a new country"""
    if not request.json or 'name' not in request.json or 'code' not in request.json:
        abort(400)
    country = Country(name=request.json['name'], code=request.json['code'])
    storage.new(country)
    storage.save()
    return jsonify(country.to_dict()), 201

