import psycopg2 as dbapi2

class Bookdetails:
    def __init__(self, id, bookid, imgurl, detail):
        self.id = id
        self.bookid= bookid
        self.imgurl=imgurl
        self.detail=detail


def insert_book_details(cursor, bookdets):
    statement = """INSERT INTO BOOKDETAILS (BOOKID, IMGURL, DETAIL) VALUES(
                %s, %s, %s
                )"""
    cursor.execute(statement, (bookdets.bookid, bookdets.imgurl, bookdets.detail,))


def get_book_imgurl(cursor, bookid):
    statement = """SELECT IMGURL FROM BOOKDETAILS WHERE (BOOKID = %s)"""
    cursor.execute(statement, (bookid))


def get_book_detail(cursor, bookid):
    statement = """SELECT DETAIL FROM BOOKDETAILS WHERE (BOOKID = %s)"""
    cursor.execute(statement, (bookid))


def update_book_details(cursor, bookid, newbook):
    statement = """ UPDATE BOOKDETAILS SET IMGURL = %(imgurl)s, DETAIL = %(detail)s WHERE BOOKID = %(bookid)s """
    cursor.execute(statement,{'imgurl':newbook.imgurl, 'detail':newbook.detail, 'bookid':bookid})

def get_book_alldetails(cursor):
    statement = """SELECT BOOKDETAILS.ID, BOOKDETAILS.BOOKID, BOOKS.TITLE, BOOKDETAILS.IMGURL, BOOKDETAILS.DETAIL FROM BOOKDETAILS INNER JOIN BOOKS ON BOOKDETAILS.BOOKID = BOOKS.ID"""
    cursor.execute(statement)
    details = cursor.fetchall()
    return details

def get_book_fulldetails(cursor):
    statement = """SELECT DETS.ID, DETS.TITLE, DETS.YEAR, DETS.AUTHOR, DETS.GENRE, BOOKDETAILS.IMGURL, BOOKDETAILS.DETAIL FROM (SELECT TB.ID, TB.TITLE, TB.YEAR, AUTHORS.NAME||' '||AUTHORS.LASTNAME AS AUTHOR, TB.NAME AS GENRE FROM (SELECT BOOKS.ID, BOOKS.TITLE, BOOKS.YEAR, BOOKS.AUTHORID, GENRES.NAME FROM BOOKS INNER JOIN GENRES ON GENRES.ID=BOOKS.GENREID)TB INNER JOIN AUTHORS ON AUTHORS.ID=TB.AUTHORID)DETS INNER JOIN BOOKDETAILS ON DETS.ID = BOOKDETAILS.BOOKID"""
    cursor.execute(statement)
    details = cursor.fetchall()
    return details

def get_book_fulldetails_byId(cursor, detailid):
    statement = """SELECT DETS.ID, DETS.TITLE, DETS.YEAR, DETS.AUTHOR, DETS.GENRE, BOOKDETAILS.IMGURL, BOOKDETAILS.DETAIL FROM (SELECT TB.ID, TB.TITLE, TB.YEAR, AUTHORS.NAME||' '||AUTHORS.LASTNAME AS AUTHOR, TB.NAME AS GENRE FROM (SELECT BOOKS.ID, BOOKS.TITLE, BOOKS.YEAR, BOOKS.AUTHORID, GENRES.NAME FROM BOOKS INNER JOIN GENRES ON GENRES.ID=BOOKS.GENREID)TB INNER JOIN AUTHORS ON AUTHORS.ID=TB.AUTHORID)DETS INNER JOIN BOOKDETAILS ON DETS.ID = BOOKDETAILS.BOOKID WHERE DETS.ID = %s"""
    cursor.execute(statement, (detailid,))
    details = cursor.fetchall()
    return details

def get_book_alldetails_byId(cursor, detailid):
    statement = """SELECT * FROM (SELECT BOOKDETAILS.ID, BOOKDETAILS.BOOKID, BOOKS.TITLE, BOOKDETAILS.IMGURL, BOOKDETAILS.DETAIL FROM BOOKDETAILS INNER JOIN BOOKS ON BOOKDETAILS.BOOKID = BOOKS.ID)TB WHERE ID = %s"""
    cursor.execute(statement, (detailid,))
    details = cursor.fetchall()
    return details