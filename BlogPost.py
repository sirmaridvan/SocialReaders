import random

class BlogPost:
    def __init__(self, id, userId, date, header, text):
        self.id = id
        self.userId = userId
        self.date=date
        self.header = header
        self.text = text

def insert_blogPost(cursor,post):
    statement = """INSERT INTO BLOGS (USERID,DATE,HEADER,TEXT) VALUES (
                %s, %s, %s, %s
                )"""
    cursor.execute(statement,(post.userId,post.date,post.header,post.text));

def getPost(cursor,id):
    statement = """SELECT ID,USERNAME,DATE,HEADER,TEXT FROM BLOGS,SITEUSER WHERE (USERID=SITEUSER.USERID) AND (ID = %(id)s)"""
    cursor.execute(statement, {'id':id})

def getAllPosts(cursor):
    statement = """SELECT ID,USERNAME,DATE,HEADER,TEXT FROM BLOGS,SITEUSER WHERE (BLOGS.USERID=SITEUSER.USERID)"""
    cursor.execute(statement)
def deletePost(cursor,id):
     statement = """DELETE FROM BLOGS WHERE (ID = %(id)s)"""
     cursor.execute(statement,{'id':id})