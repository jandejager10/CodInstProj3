from extensions import db
from models import User
from werkzeug.security import generate_password_hash

def create_default_user():
    default_user = User.query.filter_by(username='default_user').first()
    if not default_user:
        default_user = User(
            username='default_user',
            email='default_user@example.com',
            password=generate_password_hash('default_password', method='pbkdf2:sha256'),
            is_admin=True
        )
        db.session.add(default_user)
        db.session.commit()
    return default_user

if __name__ == "__main__":
    from app import app
    with app.app_context():
        user = create_default_user()
        print(f"Default user created with ID: {user.id}")
