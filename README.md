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

# Welcome
Welcome to my "Level 5 Diploma in Web Application Development" Code Institute Backend Development Milestone Project Project 3.

## Book Review and Recommendation Website
This project is a book review and recommendation website built with Flask and a relational/non-relational database. Users can create, edit, and delete book entries, write and upvote reviews, and discover new books to read.

## Project Goals
- Develop a CRUD (Create, Read, Update, Delete) application for book data.
- Implement user interaction for adding, editing, and reviewing books.
- Design a user-friendly interface with search and filtering capabilities.
- Utilize a database to store and manage book information and reviews.
- Deploy the application to a hosting platform like Heroku.

## Project Features:

### User Functionality (CRUD):
Create new book entries with details like title, author, cover image URL, and other relevant fields (genre, publication date, ISBN, etc.)
Edit existing book entries.
Write and edit reviews for books.
Upvote reviews (consider implementing a downvote option too, for balanced feedback)
Delete user-created entries (books and reviews)
### Data Model:
Design a database schema with tables for Books, Authors (if separate), Reviews, and Users (if implementing authentication).
Establish relationships between tables (e.g., a book has many reviews, a user writes many reviews)
### User Interface:
Develop a user-friendly website with a clear layout and navigation menu.
Utilize forms for user input (adding/editing books, writing reviews)
Display lists of books with search and filter options (by genre, author, etc.)
Showcase individual book pages with details, reviews, and upvote functionality.
### Deployment:
Deploy the final project to a platform like Heroku for online accessibility.
Ensure proper configuration and avoid storing sensitive information like passwords in the code repository.
### Documentation:
Create a comprehensive README.md file explaining the project functionalities, technologies used, and deployment instructions.

## Advanced Feature (Optional):
Include placeholder affiliate links for each book (demonstrate the concept without actually generating revenue).
Consider implementing user authentication for a more personalized experience (tracks user reviews, creates a watchlist, etc.)
Explore integrating with external book APIs (e.g., Goodreads) to enrich book data (synopsis, publication details)
Implement basic search functionality for users to easily find books.

## Technologies
- Frontend: HTML, CSS (Bootstrap + Materialize)
- Backend: Python + Flask
- Database: PostgreSQL hosted on [neon.tech](https://console.neon.tech/)
### Additional libraries and external APIs:
- WTForms where required or usefull
- Flask-Login (for user authentication)

## Project Structure (file layout)
- **Directories and Files:**
    - `/static` for CSS, JavaScript, and images.
    - `/templates` for HTML templates.
    - `app.py` for the main Flask application logic.
    - `models.py` for database model definitions.
    - `forms.py` for defining forms with WTForms.
    - `README.md` for project documentation.
    - `requirements.txt` for listing project dependencies.
    - `testing.md` for detailing the testing approach.


#### Database Models
- **Models (`models.py`):**
    - `User`: Stores user information.
    - `Book`: Stores book information (title, author, genre, publication date, ISBN, cover image URL).
    - `Review`: Stores reviews for books (content, upvotes, timestamps, user ID, book ID).

#### Forms with WTForms
- **Forms (`forms.py`):**
    - `BookForm`: For adding and editing book entries.
    - `ReviewForm`: For writing and editing reviews.

#### CRUD Functionality
- **Routes and View Functions:** Implement routes and logic for:
    - Adding books
    - Viewing book details
    - Editing books
    - Deleting books
    - Adding and editing reviews

#### User Authentication
- **Flask-Login Setup:** Implement user login, registration, and logout functionalities for personalized user experience.

#### HTML Templates
- **Templates (`/templates`):**
    - `base.html`: Base template for common structure.
    - `books.html`: Display list of books.
    - `add_book.html`: Form for adding new books.
    - `book_detail.html`: Display individual book details and reviews.
    - `edit_book.html`: Form for editing books.
    - `login.html`: User login form.
    - `register.html`: User registration form.

#### Front-End Styling
- **CSS Frameworks:** Use Bootstrap and Materialize for styling the web application. (might change at later stage)

#### Testing
- **Manual Testing:** See testing.md for interaction and overall user experience tests.

#### Deployment
- **Heroku Deployment:**
    - `Procfile` for Heroku.
    - Update `requirements.txt` with project dependencies.
    - Deploy the application to Heroku and configure the database.
        Database currently local for development but will be deployed either on neon.tech or code institute platform https://dbs.ci-dbs.net/

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



## Attribution
- https://www.markdownguide.org/cheat-sheet/
- Adobe, for the color wheel. #2D3540 #0B8C38 #20733D #5DBF4E #F2F2F2
- Pictures https://www.shutterstock.com/
- Favicon - https://www.shutterstock.com/
- Fonts - https://fonts.googleapis.com/
- Stylesheets and icons - https://kit.fontawesome.com
- Code usage lookups - https://www.w3schools.com/
- Forms template - https://wtforms.readthedocs.io/en/3.1.x/
- Database layout/modeling - https://stackoverflow.com/questions/21159333/database-schema-for-books-authors-publishers-and-users-with-bookshelves
- Login layout - https://www.goodreads.com/
- Review layout ideas - https://www.goodreads.com/
- Book search API - https://www.goodreads.com/api
- Code for login - https://werkzeug.palletsprojects.com/en/3.0.x/
- Code for login - https://pypi.org/project/Flask-Login/
### Media (images and animations)
    All them pictures have got to come from somewhere afterall:
- Pictures / Photos from https://stock.adobe.com/
- Favicon - https://icons8.com/

#### Version Control
- **Git:** Initialize a Git repository for version control and commit the initial project setup.

## License
This project is licensed under the MIT License - see the () file for details.

## Contact
Jan de Jager – @JdJage - jandejager10@hotmail.com
Project Link: 
