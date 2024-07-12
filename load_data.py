import json
from extensions import db
from models import Book, User

def load_data():
    with open('data/data.json') as f:
        data = json.load(f)
    
    # Get the default user
    default_user = User.query.filter_by(username='default_user').first()
    if not default_user:
        raise Exception("Default user not found. Please run create_default_user.py first.")
    
    for item in data:
        new_book = Book(
            title=item['title'],
            author=item['author'],
            genre=item['genre'],
            publication_date=item['publication_date'],
            isbn=item['isbn'],
            cover_image_url=item['cover_image_url'],
            user_id=default_user.id  # Assign the user_id of the default user
        )
        db.session.add(new_book)
    
    db.session.commit()

if __name__ == "__main__":
    from app import app
    with app.app_context():
        load_data()
        print("Data loaded successfully.")
