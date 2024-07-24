# CodInstProj3

## Code Institute Backend Development Milestone Project Project 3

## Project Requirements 
### Main Technologies
HTML, CSS, JavaScript, Python+Flask, PostgreSQL OR MongoDB

### Mandatory Requirements
A project violating any of these requirements will FAIL

- Data handling: Build a Relational OR Non-Relational Database backed Flask project for a web application that allows users to store and manipulate data records about a particular domain.
- Database structure: Put some effort into designing a database structure well-suited for your domain. Make sure to put some thought into the relationships between records of different entities.
- User functionality: Create functionality for users to create, locate, display, edit and delete records (CRUD functionality).
- Use of technologies: Use HTML and custom CSS for the website's front-end.
- Structure: Incorporate a main navigation menu and structured layout (you might want to use Materialize or Bootstrap to accomplish this).
- Documentation: Write a README.md file for your project that explains what the project does and the value that it provides to its users.
- Version control: Use Git & GitHub for version control.
- Attribution: Maintain clear separation between code written by you and code from external sources (e.g. libraries or tutorials). Attribute any code from external sources to its source via comments above the code and (for larger dependencies) in the README.
- Deployment: Deploy the final version of your code to a hosting platform such as Heroku.
- Make sure to not include any passwords or secret keys in the project repository.

## Welcome
Welcome to my "Level 5 Diploma in Web Application Development" Code Institute Backend Development Milestone Project Project 3.

## Book Review and Recommendation Website
This project is a book review and recommendation website built with Flask and a relational/non-relational database. Users can create, edit, and delete book entries, write and upvote reviews, and discover new books to read.

## Wireframes  
<p align="center">
![wireframe](static/img/am-i-responsive.png)
</p>

<p align="center">
[Visit 'Book Reviews' on Heroku](https://codeinstproj3-448813aebd4c.herokuapp.com/)
</p>

## Project Goals
- Develop a CRUD (Create, Read, Update, Delete) application for book data.
- Implement user interaction for adding, editing, and reviewing books.
- Design a user-friendly interface with search and filtering capabilities.
- Utilize a database to store and manage book information and reviews.
- Deploy the application to a hosting platform like Heroku.

## Features

### User Functionality (CRUD):
- Create new book entries with details like title, author, cover image URL, and other relevant fields (genre, publication date, ISBN, etc.)
- Edit existing book entries.
- Write and edit reviews for books.
- Upvote reviews (Page tags left in place but not implemented for actual use)
- Delete user-created entries (books and reviews)

### Data Model:
- Design a database schema with tables for Books, Authors (if separate), Reviews, and Users (if implementing authentication).
- Establish relationships between tables (e.g., a book has many reviews, a user writes many reviews)

### User Interface:
- Develop a user-friendly website with a clear layout and navigation menu.
- Utilize forms for user input (adding/editing books, writing reviews)
- Display lists of books with search and filter options (by genre, author, etc.)
- Showcase individual book pages with details, reviews, and upvote functionality.

### Deployment:
- Deploy the final project to a platform like Heroku for online accessibility.
- Ensure proper configuration and avoid storing sensitive information like passwords in the code repository.

### Documentation:
- Create a comprehensive README.md file explaining the project functionalities, technologies used, and deployment instructions.

### Advanced Feature (Optional):
- Include placeholder affiliate links for each book (demonstrate the concept without actually generating revenue).
- Consider implementing user authentication for a more personalized experience (tracks user reviews, creates a watchlist, etc.)
- Explore integrating with external book APIs (e.g., Goodreads) to enrich book data (synopsis, publication details)
- Implement basic search functionality for users to easily find books.

## Technologies
- Frontend: HTML, CSS (Materialize)
- Backend: Python + Flask
- Database: PostgreSQL hosted on [neon.tech](https://console.neon.tech/)

### Additional libraries and external APIs:
- WTForms for all forms
- Flask-Login (for user authentication)

## Project Structure (file layout)
- **Directories and Files:**
    - `/static` for CSS, JavaScript, and images.
    - `/templates` for HTML templates.
    - `/data` for preloaded database data (not in use for live project).
    - `app.py` for the main Flask application logic.
    - `models.py` for database model definitions.
    - `forms.py` for defining forms with WTForms.
    - `README.md` for project documentation.
    - `requirements.txt` for listing project dependencies.
    - `testing.md` for detailing the testing approach.
    - `create_tables.py` for creating the database tables (not in use for live project).
    - `create_default_user.py` for creating the default user and activating tables (not in use for live project).
    - `populate_user_id.py` for loading test users (not in use for live project).

## Database Models
- **Models (`models.py`):**
    - `User`: Stores user information.
    - `Book`: Stores book information (title, author, genre, publication date, ISBN, cover image URL).
    - `Review`: Stores reviews for books (content, upvotes, timestamps, user ID, book ID).

## Forms with WTForms
- **Forms (`forms.py`):**
    - `BookForm`: For adding and editing book entries.
    - `ReviewForm`: For writing and editing reviews.
    - `LoginForm`: For user login.
    - `RegistrationForm`: For user registration.

## CRUD Functionality
- **Routes and View Functions:** Implement routes and logic for:
    - Adding books
    - Viewing book details
    - Editing books
    - Deleting books
    - Adding and editing reviews

## User Authentication
- **Flask-Login Setup:** Implement user login, registration, and logout functionalities for personalized user experience.

## HTML Templates
- **Templates (`/templates`):**
    - `base.html`: Base template for common structure.
    - `books.html`: Display list of books.
    - `add_book.html`: Form for adding new books.
    - `book_detail.html`: Display individual book details and reviews.
    - `edit_book.html`: Form for editing books.
    - `edit_review.html`: Form for editing reviews.
    - `login.html`: User login form.
    - `register.html`: User registration form.
    - `index.html`: The Index page.

## Front-End Styling
- **CSS Frameworks:** Use Materialize for styling the web application.

## Testing
- **Manual Testing:** See testing.md for interaction and overall user experience tests.

## Deployment
- **Heroku Deployment:**
    - `Procfile` for Heroku.
    - Update `requirements.txt` with project dependencies.
    - Deploy the application to Heroku and configure the database.
    Database currently local for development but deployed on neon.tech for use by Heroku.

### Fields Used

#### User Model
- `id`: Unique identifier for the user.
- `username`: Username of the user.
- `email`: Email address of the user.
- `password`: Password of the user (hashed).
- `reviews`: Relationship to associate user with reviews.

#### Book Model
- `id`: Unique identifier for the book.
- `title`: Title of the book.
- `author`: Author of the book.
- `genre`: Genre of the book.
- `publication_date`: Publication date of the book.
- `isbn`: ISBN number of the book.
- `cover_image_url`: URL of the book's cover image.
- `reviews`: Relationship to associate book with reviews.

#### Review Model
- `id`: Unique identifier for the review.
- `content`: Content of the review.
- `upvotes`: Number of upvotes for the review.
- `timestamp`: Time when the review was created.
- `user_id`: ID of the user who wrote the review.
- `book_id`: ID of the book being reviewed.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/book-reviews-and-more.git
    cd book-reviews-and-more
    ```

2. **Create a virtual environment and install dependencies:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**

    Create a `.env` file in the root directory with the following content:

    ```plaintext
    SQLALCHEMY_DATABASE_URI=your_database_uri
    SECRET_KEY=your_secret_key
    ```

4. **Set up the database:**

    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

5. **Load initial data:**

    ```bash
    python load_data.py
    ```

6. **Run the application:**

    ```bash
    flask run
    ```

## Usage

- Visit the home page to browse books.
- Register for a new account or log in if you already have one.
- Add new books and reviews.
- Edit or delete your own books and reviews.
- Admin users can manage all books and reviews.

## Contributing

1. **Fork the repository:**

    ```bash
    git fork https://github.com/yourusername/book-reviews-and-more.git
    ```

2. **Create a new branch for your feature or bugfix:**

    ```bash
    git checkout -b feature-name
    ```

3. **Make your changes and commit them:**

    ```bash
    git commit -am 'Add new feature'
    ```

4. **Push to the branch:**

    ```bash
    git push origin feature-name
    ```

5. **Create a new Pull Request.**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Attribution

- **Materialize CSS:** Used for responsive design components. [Materialize CSS](https://materializecss.com/)
- **Font Awesome:** Icons used in the application. [Font Awesome](https://fontawesome.com/)
- **Google Fonts:** Custom fonts used in the application. [Google Fonts](https://fonts.google.com/)
- **Flask:** Micro web framework used to build the application. [Flask](https://flask.palletsprojects.com/)
- **SQLAlchemy:** SQL toolkit and ORM used for the database. [SQLAlchemy](https://www.sqlalchemy.org/)
- **Jinja2:** Templating engine for Flask. [Jinja2](https://palletsprojects.com/p/jinja/)

Special thanks to the following resources and contributors that helped shape the development of this application:

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Materialize CSS Documentation](https://materializecss.com/)
- [Font Awesome Documentation](https://fontawesome.com/)
- [Google Fonts Documentation](https://fonts.google.com/)
- [SQLAlchemy Documentation](https://www.sqlalchemy.org/)
- [Jinja2 Documentation](https://palletsprojects.com/p/jinja/)

### Media (images and animations)
- All them pictures have got to come from somewhere afterall:
- Pictures - https://images-na.ssl-images-amazon.com/
- Favicon - https://icons8.com/

For any issues or questions, please feel free to open an issue on the GitHub repository.

## Contact
Jan de Jager – @JdJage - jandejager10@hotmail.com
Project Link: 
