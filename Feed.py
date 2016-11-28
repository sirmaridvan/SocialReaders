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
