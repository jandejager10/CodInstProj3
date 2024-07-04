import json
from app import app, db
from models import User, Book
from werkzeug.security import generate_password_hash

def load_data():
    with open('data/data.json') as json_file:
        data = json.load(json_file)

        # Load books
        for item in data['books']:
            book = Book(
                title=item['title'],
                author=item['author'],
                genre=item['genre'],
                publication_date=item['publication_date'],
                isbn=item['isbn'],
                cover_image_url=item['cover_image_url']
            )
            db.session.add(book)

        # Load users
        for item in data['users']:
            hashed_password = generate_password_hash(item['password'], method='pbkdf2:sha256')
            user = User(
                username=item['username'],
                email=item['email'],
                password=hashed_password
            )
            db.session.add(user)

        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        load_data()
