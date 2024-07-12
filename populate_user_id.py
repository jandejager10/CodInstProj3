from app import app, db
from models import Book, User

def populate_user_id():
    with app.app_context():
        # Get the default user (e.g., the first user in the table)
        default_user = User.query.first()
        
        if default_user:
            # Update all books with the default user's ID
            books = Book.query.filter_by(user_id=None).all()
            for book in books:
                book.user_id = default_user.id
                db.session.add(book)
            db.session.commit()
        else:
            print("No default user found. Please create a user first.")

if __name__ == "__main__":
    populate_user_id()
