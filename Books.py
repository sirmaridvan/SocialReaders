import psycopg2 as dbapi2

class Book:
    def __init__(self, id, title, year, author_id, genre_id):
        self.id = id
        self.title= title
        self.year=year
        self.author_id=author_id
        self.genre_id=genre_id

def insert_book(dsn, book):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """INSERT INTO BOOKS (TITLE,YEAR,AUTHORID,GENREID) VALUES (
                %s, %s, %s, %s
                )"""
        cursor.execute(statement,(book.title, book.year, book.author_id, book.genre_id,))
        cursor.close()


def selectBook(dsn):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """SELECT * FROM BOOKS ORDER BY ID ASC"""
        cursor.execute(statement)
        books = cursor.fetchall()
        return books
        cursor.close()

def selectBookwithJoin(dsn):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """SELECT TB.ID, TB.TITLE, TB.YEAR, AUTHORS.NAME AS AUTHOR, TB.NAME AS GENRE FROM (SELECT BOOKS.ID, BOOKS.TITLE, BOOKS.YEAR, BOOKS.AUTHORID, GENRES.NAME FROM BOOKS INNER JOIN GENRES ON GENRES.ID=BOOKS.GENREID)TB INNER JOIN AUTHORS ON AUTHORS.ID=TB.AUTHORID"""
        cursor.execute(statement)
        books = cursor.fetchall()
        return books
        cursor.close()


def selectBookbyID(dsn, id):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """SELECT * FROM BOOKS WHERE ID = %s"""
        cursor.execute(statement,(id,))
        books = cursor.fetchall()
        return books
        cursor.close()

def selectBookbyTitle(dsn, title):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """SELECT * FROM BOOKS WHERE TITLE = %s"""
        cursor.execute(statement,(title,))
        books = cursor.fetchall()
        return books
        cursor.close()

def selectBookbyYear(dsn, year):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """SELECT * FROM BOOKS WHERE YEAR = %s"""
        cursor.execute(statement,(year,))
        books = cursor.fetchall()
        return books
        cursor.close()

def selectBookbyAuthor(dsn, author_id):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """SELECT * FROM BOOKS WHERE AUTHORID = %s"""
        cursor.execute(statement,(author_id,))
        books = cursor.fetchall()
        return books
        cursor.close()

def selectBookbyGenre(dsn, genre_id):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """SELECT * FROM BOOKS WHERE GENREID = %s"""
        cursor.execute(statement,(genre_id,))
        books = cursor.fetchall()
        return books
        cursor.close()

def deleteBook(dsn, id):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """DELETE FROM BOOKS WHERE ID = %s """
        cursor.execute(statement,(id,))
        cursor.close()

def updateBook(dsn, id, newbook):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ UPDATE BOOKS SET TITLE = %s YEAR = %s AUTHORID = %s GENREID = %s WHERE ID = %s """
        cursor.execute(statement,(newbook.title, newbook.year, newbook.author_id, newbook.genre_id, id,))
        cursor.close()