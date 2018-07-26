# CS50x Web Programming with Python and JavaScript

## Project 1

### Python Flask Web Application: Book Review site

This web application fulfills the requirements of the Harvard University CS50x Web Programming course on edX.

The technologies used/demonstrated are:

* Python 3.6
* Flask
* SQL (PostgreSQL)
* SQLAlchemy (non-ORM)
* Git
* Heroku web hosting
* HTML5
* Jinja2 templates
* APIs, both using an API (Goodreads) and creating an API

you can view the application at [Project1 Book Review Site](https://cs50wproject1.herokuapp.com)

Files:

* application.py ... the python views and helper functions, plus db engine connection code, etc.
* index.html ... root of the url. The user generally only sees this once per session. It contains 2 links: one to Login, and one to Register.
* login.html ... form for user to input name and password.
* register.html ... form for a new user to register a new user name and password.
* logout.html ... just says "you are now logged out" and provides a button to login again.
* search.html ... form for search functionality
* result.html ... provides a table of search results and links to book details.
* book.html ... shows book details, including Goodreads data (number of reviews on Goodreads for this book, and the average rating the book has on Goodreads). book.html also provides a field for the user to type a review for the current book and an input, limited to numbers 1 to 5, for the user to rate the book.
* other_reviews.html ... shows a table of the reviews for the current book on this site. If the user has just written a review it appears at the top of this list.
* error.html ... shows an error message if user tries to log in when they are already logged in. Provides a "Search again" button.
* layout.html ... base HTML that all the other HTML files inherit from.
* style.css ... some minimal css.
