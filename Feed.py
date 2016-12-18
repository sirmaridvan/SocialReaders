class Feed:
    def __init__(self, id, date, userId, bookId, typeId):
        self.id = id
        self.date=date
        self.userId = userId
        self.bookId = bookId
        self.typeId = typeId

def insert_feed(cursor,feed):
    statement = """INSERT INTO FEEDS (DATE,USERID,BOOKID,TYPEID) VALUES (
                %s, %s, %s, %s
                )"""
    cursor.execute(statement,(feed.date,feed.userId,feed.bookId,feed.typeId));
def get_all_feeds(cursor):
    statement = """SELECT FEEDS.DATE, SITEUSER.USERNAME, BOOKS.TITLE, FEEDTYPES.TYPE FROM FEEDS, SITEUSER, BOOKS, FEEDTYPES
                    WHERE (FEEDS.USERID=SITEUSER.USERID) AND (FEEDS.BOOKID=BOOKS.ID) AND (FEEDS.TYPEID=FEEDTYPES.ID) """
    cursor.execute(statement);
def get_like_number_of_book(cursor,bookId):
    statement = """ SELECT COUNT(ID) FROM FEEDS WHERE (BOOKID = %(bookId)s) AND (TYPEID=1)"""
    cursor.execute(statement,{'bookId':bookId});
def get_suggestion_number_of_book(cursor,bookId):
    statement = """ SELECT COUNT(ID) FROM FEEDS WHERE (BOOKID = %(bookId)s) AND (TYPEID=2)"""
    cursor.execute(statement,{'bookId':bookId});

def get_like_number_of_all_books(cursor):
    statement = """ SELECT BOOKID, COUNT(ID) AS LIKE FROM FEEDS WHERE (TYPEID = 1) GROUP BY BOOKID """
    cursor.execute(statement)

def get_suggestion_number_of_all_books(cursor):
    statement = """ SELECT BOOKID, COUNT(ID) AS SUGGESTION FROM FEEDS WHERE (TYPEID = 2) GROUP BY BOOKID """
    cursor.execute(statement)

def check_if_feeded(cursor, feed):
    statement = """ SELECT COUNT(ID) FROM FEEDS WHERE (USERID = %s) AND (BOOKID = %s) AND (TYPEID = %s) """
    cursor.execute(statement,(feed.userId, feed.bookId, feed.typeId))
    ret = cursor.fetchall()
    return ret

