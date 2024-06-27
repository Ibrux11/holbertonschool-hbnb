import pytest
from app import app, db
from models import User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_user_creation(client):
    user = User(email='test@example.com', password='password123')
    db.session.add(user)
    db.session.commit()
    assert user.id is not None

def test_user_retrieval(client):
    user = User(email='test@example.com', password='password123')
    db.session.add(user)
    db.session.commit()
    retrieved_user = User.query.filter_by(email='test@example.com').first()
    assert retrieved_user is not None
    assert retrieved_user.email == 'test@example.com'
