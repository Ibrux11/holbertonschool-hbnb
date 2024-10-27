#!/usr/bin/python3

from sqlalchemy import exc
from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade  # Facade pour la logique de gestion des reviews

# Création de la namespace Flask-RESTx pour les reviews
api = Namespace('reviews', description='Operations related to reviews')

# Définition du modèle de données pour les reviews dans l'API
review_model = api.model('Review', {
    'user_id': fields.Integer(required=True, description="ID de l'utilisateur"),
    'place_id': fields.Integer(required=True, description="ID du lieu"),
    'rating': fields.Integer(required=True, min=1, max=5, description="Note entre 1 et 5"),
    'text': fields.String(required=True, description="Contenu de l'avis")
})

# Instanciation de la Facade pour l'accès aux méthodes métier
facade = HBnBFacade()

@api.route('/')
class ReviewListResource(Resource):
    @api.marshal_list_with(review_model)
    def get(self):
        """Récupérer toutes les reviews (pagination par défaut)"""
        return facade.get_all_reviews()

    @api.expect(review_model)
    @api.marshal_with(review_model)
    def post(self):
        """Créer une nouvelle review"""
        review_data = api.payload
        return facade.create_review(review_data)

@api.route('/<int:review_id>')
@api.param('review_id', 'L\'ID de la review')
class ReviewResource(Resource):
    @api.marshal_with(review_model)
    def get(self, review_id):
        """Récupérer une review par ID"""
        return facade.get_review(review_id)

    @api.expect(review_model)
    @api.marshal_with(review_model)
    def put(self, review_id):
        """Mettre à jour une review existante"""
        review_data = api.payload
        return facade.update_review(review_id, review_data)

    def delete(self, review_id):
        """Supprimer logiquement une review"""
        return facade.delete_review(review_id)

@api.route('/place/<int:place_id>')
@api.param('place_id', 'L\'ID du lieu')
class PlaceReviewResource(Resource):
    @api.marshal_list_with(review_model)
    def get(self, place_id):
        """Récupérer toutes les reviews pour un lieu donné"""
        return facade.get_reviews_by_place(place_id)
