import random

class BlogPost:
    def __init__(self, id, userName, date, header, text):
        self.id = id
        self.userName = userName
        self.date=date
        self.header = header
        self.text = text

def createRandomUserName():
    ALPHABET = "0123456789ABCDEFGHJIKLMNOPQRSTUVQXYZabcdefghijklmnopqrstuvwxyz"
    chars=[]
    for i in range(3):
        chars.append(random.choice(ALPHABET))
    return chars

def insert_blogPost(cursor,post):
    statement = """INSERT INTO BLOGS (USERNAME,DATE,HEADER,TEXT) VALUES (
                %s, %s, %s, %s
                )"""
    cursor.execute(statement,(post.userName,post.date,post.header,post.text));

def getPost(cursor,id):
    statement = """SELECT ID,USERNAME,DATE,HEADER,TEXT FROM BLOGS WHERE (ID = %(id)s)"""
    cursor.execute(statement, {'id':id})

def getAllPosts(cursor):
    statement = """SELECT ID,USERNAME,DATE,HEADER,TEXT FROM BLOGS"""
    cursor.execute(statement)
    return cursor