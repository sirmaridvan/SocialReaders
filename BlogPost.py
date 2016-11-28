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
    statement = """SELECT ID,USERNAME,DATE,HEADER,TEXT FROM BLOGS,SITEUSER WHERE (BLOGS.USERID=SITEUSER.USERID) AND (ID = %(id)s)"""
    cursor.execute(statement, {'id':id})

def getAllPosts(cursor):
    statement = """SELECT ID,BLOGS.USERID,USERNAME,DATE,HEADER,TEXT FROM BLOGS,SITEUSER WHERE (BLOGS.USERID=SITEUSER.USERID)"""
    cursor.execute(statement)
def deletePost(cursor,id):
     statement = """DELETE FROM BLOGS WHERE (ID = %(id)s)"""
     cursor.execute(statement,{'id':id})
def updatePost(cursor,text,id,date):
    statement = """UPDATE BLOGS SET TEXT=%(text)s, DATE=%(date)s WHERE (ID = %(id)s)"""
    cursor.execute(statement,{'text':text,'date':date,'id':id})
def getUserIdFromId(cursor,id):
    statement = """SELECT USERID FROM BLOGS WHERE (ID = %(id)s)"""
    cursor.execute(statement,{'id':id})