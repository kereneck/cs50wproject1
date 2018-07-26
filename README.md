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

* **application.py** ... the python views and helper functions, plus db engine connection code, etc.
* **index.html** ... root of the url. The user generally only sees this once per session. It contains 2 links: one to Login, and one to Register. The user can only get back to this page if they manually edit the url.
* **login.html** ... form for user to input name and password. Also provides a link to the registration page in case a user chooses Login at the index page (or if they enter the site url and put "/login" on the end of it) before they have an account.
* **register.html** ... form for a new user to register a new user name and password.
* **logout.html** ... just says "you are now logged out" and provides a button to login again.
* **search.html** ... form for search functionality. The user can enter either a title, an author, or an ISBN, or any combination of these. Partial search terms are also catered for. If a user fills in more than one search field then the ISBN field takes precedence, followed by the title field, and lastly the author field. [This needs fixing because it gives the impression that all the search terms matter when in fact if there's an ISBN the other search fields are ignored.] If no fields are filled in an error message is produced asking the user to fill in at least one of the fields. This error message appears on the search page itself.
* **results.html** ... provides a table of search results and links to book details.
* **book.html** ... shows book details, including Goodreads data (number of reviews on Goodreads for this book, and the average rating the book has on Goodreads). book.html also provides a field for the user to type a review for the current book and an input, limited to numbers 1 to 5, for the user to rate the book. If a user has already submitted a review and rating for the current book then the review and rating inputs do not appear on this page. Users are therefor limited to one review per book. After the user submits a review he or she is taken to the other_reviews page. There is a separate button to display the reviews for the book. This page also provides a "Search again" button.
* **other_reviews.html** ... shows a table of the reviews for the current book on this site. If the user has just written a review it appears at the top of this list.
* **no_results.html** ... if there are no search results this page is shown. Provides a "Search again" button.
* **error.html** ... shows an error message if user tries to log in when they are already logged in. Provides a "Search again" button.
* **layout.html** ... base HTML that all the other HTML files inherit from.
* **style.css** ... some minimal css.

All pages, except index.html, login.html, logout.html and register.html, display the logged in user's username at the top left, and a "Logout" button at the top right.
