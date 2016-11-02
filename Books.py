class Book:
    def __init__(self, bookid, title, year, author_id, genre_id):
        self.bookid = bookid
        self.title= title
        self.year=year
        self.author_id=author_id
        self.genre_id=genre_id

def insert_book(cursor, book):
        statement = """INSERT INTO BOOKS (TITLE,YEAR,AUTHORID,GENREID) VALUES (
                %s, %s, %s, %s
                )"""
        cursor.execute(statement,(book.title, book.year, book.author_id, book.genre_id))


def select_books(cursor):
        statement = """SELECT * FROM BOOKS ORDER BY ID ASC"""
        cursor.execute(statement)

def select_bookid(cursor, bookid):
        statement = """SELECT * FROM BOOKS WHERE BOOKID = %s"""
        cursor.execute(statement)

def select_booktitle(cursor, title):
        statement = """SELECT * FROM BOOKS WHERE TITLE = %s"""
        cursor.execute(statement)

def select_bookyear(cursor, year):
        statement = """SELECT * FROM BOOKS WHERE YEAR = %s"""
        cursor.execute(statement)

def select_bookauthorid(cursor, author_id):
        statement = """SELECT * FROM BOOKS WHERE AUTHORID = %s"""
        cursor.execute(statement)

def select_bookgenreid(cursor, genre_id):
        statement = """SELECT * FROM BOOKS WHERE GENREID = %s"""
        cursor.execute(statement)

def delete_book(cursor, bookid):
        statement = """DELETE FROM BOOKS WHERE BOOKID = %s """
        cursor.execute(statement)

def update_book(cursor, bookid):
        statement = """ UPDATE BOOKS SET TITLE = %s YEAR = %s AUTHORID = %s GENREID = %s WHERE BOOKID = %s """
        cursor.execute(statement)