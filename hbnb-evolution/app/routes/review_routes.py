#!/usr/bin/python3
"""Routes for Review"""

from flask import Blueprint, jsonify, request, abort
from models import storage
from models.review import Review

review_routes = Blueprint('review_routes', __name__)

@review_routes.route('/reviews', methods=['GET'])
def get_reviews():
    """Retrieve all reviews"""
    reviews = storage.all(Review)
    return jsonify([review.to_dict() for review in reviews])

@review_routes.route('/reviews', methods=['POST'])
def create_review():
    """Create a new review"""
    if not request.json or 'user_id' not in request.json or 'place_id' not in request.json or 'rating' not in request.json or 'comment' not in request.json:
        abort(400)
    review = Review(
        user_id=request.json['user_id'],
        place_id=request.json['place_id'],
        rating=request.json['rating'],
        comment=request.json['comment']
    )
    storage.new(review)
    storage.save()
    return jsonify(review.to_dict()), 201

