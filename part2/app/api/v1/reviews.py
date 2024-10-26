#!/usr/bin/python3

from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'title': fields.String(required=True, description='Title of the review'),
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

facade = HBnBFacade()


@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        review_data = api.payload
        user = review_data['user_id']
        if user is None:
            return {'error': 'Invalid user ID'}, 400
        place = review_data['place_id']
        if place is None:
            return {'error': 'Invalid place ID'}, 400
        new_review = facade.create_review(review_data)
        return {
            'id': new_review.id,
            'title': new_review.title,
            'rating': new_review.rating
        }, 201

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        review = facade.get_all_reviews()
        return [{'title': review.title} for review in review], 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        review = facade.get_review(review_id)
        print(review)
        if not review:
            return {'error': 'review not found'}, 404
        return {'id': review.id, 'title': review.title}, 200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review's information"""
        review_data = api.payload
        updated_review = facade.update_review(review_id, review_data)
        if not updated_review:
            return {'error': 'review not found'}, 404
        return {'id': updated_review.id, 'title': updated_review.title}, 200


    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        success = facade.delete_review(review_id)
        if not success:
            return {'message': 'Review not found'}, 404
        return {'message': 'Review deleted successfully'}, 200

    @api.route('/places/<place_id>/reviews')
    class PlaceReviewList(Resource):
        @api.response(200, 'List of reviews for the place retrieved successfully')
        @api.response(404, 'Place not found')
        def get(self, place_id):
            """Get all reviews for a specific place"""
            reviews = facade.get_reviews_by_place(place_id)
            if not reviews:
                return {'message': 'Place not found or no reviews for this place'}, 404
            reviews_list = [{
                'id': review.id,
                'text': review.text,
                'rating': review.rating,
                'user': review.user.id,
                'created_at': review.created_at.isoformat(),
                'updated_at': review.updated_at.isoformat()
            } for review in reviews]
            return reviews_list