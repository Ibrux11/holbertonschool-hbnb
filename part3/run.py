#!/usr/bin/python3

from app import create_app
from extensions import db
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review

# Create the app instance
app = create_app()

# Create all tables if they do not exist (inside app context)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)