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
