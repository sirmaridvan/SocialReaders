import random

class Feed:
    def __init__(self, id, date, userName, description):
        self.id = id
        self.date=date
        self.userName = userName
        self.description = description

def insert_feed(cursor,feed):
    statement = """INSERT INTO FEEDS (DATE,USERNAME,DESCRIPTION) VALUES (
                %s, %s, %s
                )"""
    cursor.execute(statement,(feed.date,feed.userName,feed.description));
