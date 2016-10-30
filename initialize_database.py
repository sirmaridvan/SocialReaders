import psycopg2 as dbapi2


def drop_tables(cursor):
    statement = """
                DROP TABLE IF EXISTS SITEUSER CASCADE;
                DROP TABLE IF EXISTS USERTYPE CASCADE;
                """
    cursor.execute(statement)

def create_usertype_table(cursor):
    statement = """CREATE TABLE USERTYPE (
                ID SERIAL PRIMARY KEY,
                TYPE VARCHAR(8) NOT NULL
                )"""
    cursor.execute(statement);

def create_blogs_table(cursor):
    statement = """CREATE TABLE IF NOT EXISTS BLOGS (
                ID SERIAL PRIMARY KEY,
                USERNAME VARCHAR(20) NOT NULL,
                DATE DATE NOT NULL DEFAULT CURRENT_DATE,
                HEADER VARCHAR(20) NOT NULL,
                TEXT TEXT NOT NULL
                )"""
    cursor.execute(statement);

def create_jobs_table(cursor):
    statement = """CREATE TABLE IF NOT EXISTS JOBS (
                ID SERIAL PRIMARY KEY,
                DATE DATE NOT NULL DEFAULT CURRENT_DATE,
                HEADER VARCHAR(20) NOT NULL,
                DESCRIPTION TEXT NOT NULL
                )"""
    cursor.execute(statement);

def create_user_table(cursor):
    statement = """CREATE TABLE SITEUSER (
                USERID SERIAL PRIMARY KEY,
                USERNAME VARCHAR(20) UNIQUE NOT NULL,
                SALT VARCHAR(40) UNIQUE NOT NULL,
                HASH VARCHAR(44) NOT NULL,
                EMAIL VARCHAR(40) NOT NULL,
                NAME VARCHAR(20) NOT NULL,
                SURNAME VARCHAR(20) NOT NULL,
                USERTYPEID INTEGER REFERENCES USERTYPE(ID) ON UPDATE CASCADE
                )"""
    cursor.execute(statement)

''' Author table '''

dsn = """user='vagrant' password='vagrant'
         host='localhost' port=5432 dbname='itucsdb'"""

def create_author_table():
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ CREATE TABLE IF NOT EXISTS AUTHORS(
            ID SERIAL PRIMARY KEY,
            NAME VARCHAR(50) NOT NULL,
            LASTNAME VARCHAR(50) NOT NULL,
            BIRTHDATE NUMERIC(4) NOT NULL,
            NATIONALITY VARCHAR(50) NOT NULL,
            PENNAME VARCHAR(50)
        )"""
        cursor.execute(statement)
        cursor.close()


def insert_author(author):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ INSERT INTO AUTHORS (NAME, LASTNAME, BIRTHDATE, NATIONALITY, PENNAME) VALUES (%s,%s,%s,%s,%s)"""
        cursor.execute(statement,(author.name,author.lastname,author.birthdate,author.nationality,author.penname))
        cursor.close()


''' Book Table'''

def create_book_table(cursor):
    statement = """CREATE TABLE BOOKS (
                BOOKID SERIAL PRIMARY KEY,
                TITLE VARCHAR(40) NOT NULL,
                YEAR NUMERIC(4) NOT NULL,
                AUTHORID NUMERIC(4) NOT NULL,
                GENREID NUMERIC(4) NOT NULL
                )"""
    cursor.execute(statement)


def insert_book(book):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ INSERT INTO BOOKS (TITLE, YEAR, AUTHORID, GENREID) VALUES (%s,%s,%s,%s)"""
        cursor.execute(statement,(book.title, book.year, book.author_id, book.genre_id))
        cursor.close()


''' Genre Table'''

def create_genre_table(cursor):
    statement = """CREATE TABLE GENRES (
                GENREID SERIAL PRIMARY KEY,
                GENRENAME VARCHAR(20) NOT NULL
                )"""
    cursor.execute(statement)


def insert_genre(genre):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ INSERT INTO GENRES (GENRENAME) VALUES (%s)"""
        cursor.execute(statement,(genre.genre_name))
        cursor.close()


''' Quote Table'''

def create_quote_table(cursor):
    statement = """CREATE TABLE QUOTES (
                QUOTEID SERIAL PRIMARY KEY,
                QUOTETEXT VARCHAR(200) NOT NULL,
                AUTHORID NUMERIC(4) NOT NULL,
                BOOKID NUMERIC(4) NOT NULL
                )"""
    cursor.execute(statement)


def insert_quote(quote):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ INSERT INTO QUOTES (QUOTETEXT, AUTHORID, BOOKID) VALUES (%s, %s, %s)"""
        cursor.execute(statement,(quote.quotetext, quote.author_id, quote.book_id))
        cursor.close()

