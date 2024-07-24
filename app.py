from flask import Flask, render_template, redirect, url_for, request, flash
from extensions import db, migrate, login_manager
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Login Manager
db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)
login_manager.login_view = 'login'

# Import models after initializing db to avoid circular imports
from models import User, Book, Review
from forms import BookForm, ReviewForm, LoginForm, RegistrationForm


# User loader callback function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Routes
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/books', methods=['GET', 'POST'])
def books():
    form = BookForm()
    if form.validate_on_submit():
        new_book = Book(
            title=form.title.data,
            author=form.author.data,
            genre=form.genre.data,
            publication_date=form.publication_date.data,
            isbn=form.isbn.data,
            cover_image_url=form.cover_image_url.data
        )
        db.session.add(new_book)
        db.session.commit()
        flash('Book added successfully', 'success')
        return redirect(url_for('books'))
    books = Book.query.all()
    return render_template('books.html', form=form, books=books)


@app.route('/book/<int:book_id>', methods=['GET', 'POST'])
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    form = ReviewForm()
    if form.validate_on_submit():
        new_review = Review(
            content=form.content.data,
            user_id=current_user.id,
            book_id=book.id
        )
        db.session.add(new_review)
        db.session.commit()
        flash('Review added successfully', 'success')
        return redirect(url_for('book_detail', book_id=book.id))
    reviews = Review.query.filter_by(book_id=book.id).all()
    return render_template('book_detail.html',
                           book=book, form=form, reviews=reviews)


@app.route('/book/edit/<int:book_id>', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)
    if book.user_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to edit this book', 'danger')
        return redirect(url_for('book_detail', book_id=book.id))

    form = BookForm(obj=book)
    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        book.genre = form.genre.data
        book.publication_date = form.publication_date.data
        book.isbn = form.isbn.data
        book.cover_image_url = form.cover_image_url.data
        db.session.commit()
        flash('Book updated successfully', 'success')
        return redirect(url_for('book_detail', book_id=book.id))

    return render_template('edit_book.html', form=form, book=book)


@app.route('/review/edit/<int:review_id>', methods=['GET', 'POST'])
@login_required
def edit_review(review_id):
    review = Review.query.get_or_404(review_id)
    if review.user_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to edit this review', 'danger')
        return redirect(url_for('book_detail', book_id=review.book_id))

    form = ReviewForm(obj=review)
    if form.validate_on_submit():
        review.content = form.content.data
        db.session.commit()
        flash('Review updated successfully', 'success')
        return redirect(url_for('book_detail', book_id=review.book_id))

    return render_template('edit_review.html', form=form, review=review)


@app.route('/review/delete/<int:review_id>', methods=['POST'])
@login_required
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    if review.user_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to delete this review', 'danger')
        return redirect(url_for('book_detail', book_id=review.book_id))
    db.session.delete(review)
    db.session.commit()
    flash('Review deleted successfully', 'success')
    return redirect(url_for('book_detail', book_id=review.book_id))


@app.route('/book/delete/<int:book_id>', methods=['POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    if not current_user.is_admin:
        flash('You do not have permission to delete this book', 'danger')
        return redirect(url_for('books'))
    db.session.delete(book)
    db.session.commit()
    flash('Book deleted successfully', 'success')
    return redirect(url_for('books'))


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        new_book = Book(
            title=form.title.data,
            author=form.author.data,
            genre=form.genre.data,
            publication_date=form.publication_date.data,
            isbn=form.isbn.data,
            cover_image_url=form.cover_image_url.data,
            user_id=current_user.id  # Set user_id to current logged-in user
        )
        db.session.add(new_book)
        db.session.commit()
        flash('Book added successfully', 'success')
        return redirect(url_for('books'))
    return render_template('add_book.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Check username and password', 'danger')
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256'
        )
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Account created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
