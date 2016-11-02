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
