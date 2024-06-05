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
- Frontend: HTML, CSS (Bootstrap/Materialize - optional)
- Backend: Python + Flask
- Database: PostgreSQL/MongoDB (to be decided)
### Additional libraries and external APIs:
- WTForms (maybe)
- Flask-Login (optional: for user authentication)

## Project Structure (file layout)
- app.py: Main Flask application file.
- templates: Directory containing HTML templates for different website pages.
- static: Directory for static files like CSS and JavaScript.
- models.py: Python file defining database models (Books, Reviews, etc.)
- forms.py: Python file defining user input forms (add/edit book, write review).
- README.md: This file (currently editing and updating as I go).
- requirements.txt: Text file listing project dependencies.
- data/company.json: will define the database models
- templates/base.html: the base html file
- templates/books.html:  for browsing books
- templates/add_book.html: for adding new books and more
...(other folders/files as needed)
### Current Progress (Update as you go)
Briefly describe the current state of the project. What functionalities are implemented?
Mention any specific features you've completed or are currently working on.
Note any challenges encountered and solutions implemented.


## Example for what this should look like:
CRUD functionality for books is complete (add, edit, delete book entries).
User can write and edit reviews for existing books.
Basic search functionality for books by title is implemented.
Currently working on upvote functionality for reviews.
Deployment (Update when deployed)
The application is deployed on Heroku (or other platform, specify URL).
Instructions on accessing the deployed application (if applicable).

## Attribution
- https://www.markdownguide.org/cheat-sheet/
- Adobe, for the color wheel. #2D3540 #0B8C38 #20733D #5DBF4E #F2F2F2
- Pictures https://www.shutterstock.com/
- Favicon - https://www.shutterstock.com/
- Fonts - https://fonts.googleapis.com/
- Stylesheets and icons - https://kit.fontawesome.com
- Code usage lookups - https://www.w3schools.com/
- Forms template - https://wtforms.readthedocs.io/en/3.1.x/
### Media (images and animations)
    All them pictures have got to come from somewhere afterall:
- Pictures / Photos from https://stock.adobe.com/
- Favicon - https://icons8.com/

## Release History

## Next Steps
Outline your plans for further development of the project.
Mention any additional features you plan to implement.
Contributing (Optional)
Include instructions for contributing to the project (if applicable).
Specify code style guidelines or testing procedures to follow.

## License
This project is licensed under the MIT License - see the () file for details.

## Contact
Jan de Jager – @JdJage - jandejager10@hotmail.com
Project Link: 
