import csv
import os

from sqlalchemy import create_engine

# Not allowed to use ORM n this project
from sqlalchemy.orm import scoped_session, sessionmaker

# Use this for filling the books table in your Heroku-hosted db:
#engine = create_engine(os.getenv("DATABASE_URL"))
# Use this for local db we're going to create:
engine = create_engine("postgresql+psycopg2://postgres:zap123@localhost/books")

db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    next(reader, None)

    for isbn, title, author, year in reader:

        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn,:title,:author,:year)",
                    {"isbn": isbn, "title": title, "author": author, "year": year})
        print(f"Added book {isbn} : {title} : {author} : {year}.")
        
    db.commit()


if __name__ == "__main__":
    main()
