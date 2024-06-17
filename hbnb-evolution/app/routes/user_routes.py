#!/usr/bin/python3
"""Routes for User"""

from flask import Blueprint, jsonify, request, abort
from models import storage
from models.user import User

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['GET'])
def get_users():
    """Retrieve all users"""
    users = storage.all(User)
    return jsonify([user.to_dict() for user in users])

@user_routes.route('/users', methods=['POST'])
def create_user():
    """Create a new user"""
    if not request.json or 'email' not in request.json or 'password' not in request.json:
        abort(400)
    user = User(
        email=request.json['email'],
        password=request.json['password'],
        first_name=request.json.get('first_name', ""),
        last_name=request.json.get('last_name', "")
    )
    storage.new(user)
    storage.save()
    return jsonify(user.to_dict()), 201

