from sqlalchemy.orm import exc

class HBnBFacade:
    def create_review(self, review_data):
        # Validate the presence of user_id, place_id, and rating
        try:
            user = User.query.get(review_data.get('user_id'))
            place = Place.query.get(review_data.get('place_id'))
            if not user or not place:
                raise ValueError('Invalid user_id or place_id')

            # Validate rating is between 1 and 5
            if not (1 <= review_data['rating'] <= 5):
                raise ValueError('Rating must be between 1 and 5')

            # Validate text field is not empty and has a reasonable length
            if not review_data.get('text') or len(review_data['text']) > 500:
                raise ValueError('Review text must be present and less than 500 characters')

            # Create and save the review within a transaction
            review = Review(**review_data)
            db.session.add(review)
            db.session.commit()
            return review

        except exc.SQLAlchemyError as e:
            db.session.rollback()  # Rollback transaction on failure
            raise ValueError(f"Error during database transaction: {e}")

    def get_review(self, review_id):
        try:
            review = Review.query.get(review_id)
            if not review:
                raise ValueError('Review not found')
            return review

        except exc.SQLAlchemyError as e:
            raise ValueError(f"Error fetching review: {e}")

    def get_all_reviews(self, page=1, per_page=10):
        try:
            # Paginate the reviews to avoid performance issues with large datasets
            paginated_reviews = Review.query.paginate(page, per_page, error_out=False)
            return paginated_reviews.items

        except exc.SQLAlchemyError as e:
            raise ValueError(f"Error fetching all reviews: {e}")

    def get_reviews_by_place(self, place_id, page=1, per_page=10):
        try:
            place = Place.query.get(place_id)
            if not place:
                raise ValueError('Place not found')
            
            # Paginate the reviews by place
            paginated_reviews = place.reviews.paginate(page, per_page, error_out=False)
            return paginated_reviews.items

        except exc.SQLAlchemyError as e:
            raise ValueError(f"Error fetching reviews for place: {e}")

    def update_review(self, review_id, review_data):
        try:
            review = Review.query.get(review_id)
            if not review:
                raise ValueError('Review not found')

            # Validate rating if it is being updated
            if 'rating' in review_data and not (1 <= review_data['rating'] <= 5):
                raise ValueError('Rating must be between 1 and 5')

            # Update the review with the new data
            for key, value in review_data.items():
                setattr(review, key, value)
            db.session.commit()
            return review

        except exc.SQLAlchemyError as e:
            db.session.rollback()
            raise ValueError(f"Error updating review: {e}")

    def delete_review(self, review_id):
        try:
            review = Review.query.get(review_id)
            if not review:
                raise ValueError('Review not found')

            # Logical delete: mark the review as deleted instead of removing it from the database
            review.is_deleted = True
            db.session.commit()
            return True

        except exc.SQLAlchemyError as e:
            db.session.rollback()
            raise ValueError(f"Error deleting review: {e}")

'''
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
        
'''