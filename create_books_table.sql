CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    isbn VARCHAR NOT NULL,
    title VARCHAR NOT NULL,
    author VARCHAR NOT NULL,
    year VARCHAR NOT NULL
);




/* ultimately we need to deal with reviews and be able to return review_count
and average_score in our json via our API

Useful incantations:
richard@salander$ sudo -i -u postgres
postgres@salander$ createdb books
postgres@salander$ psql books
books=# [SQL commands]
books=# \d
books=# \q
postgres@salander$ exit
richard@salander$ ...
*/
