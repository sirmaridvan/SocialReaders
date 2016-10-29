import hashlib
import random

class User:
    def __init__(self, userId, userName, password, salt, hash, email, name, surname, userTypeId):
        self.userId = userId
        self.userName = userName
        self.password = password
        self.salt = salt
        self.hash = hash
        self.email = email
        self.name = name
        self.surname = surname
        self.userTypeId = userTypeId

def createRandomSalt():
    ALPHABET = "0123456789ABCDEFGHJIKLMNOPQRSTUVQXYZabcdefghijklmnopqrstuvwxyz"
    chars=[]
    for i in range(10):
        chars.append(random.choice(ALPHABET))
    return chars

def createHash(salt,password):
    hash_object = hashlib.sha1(password.join(salt).encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig

def insert_usertype(cursor,type):
    statement = """INSERT INTO USERTYPE (TYPE) VALUES (
                %(type)s
                )"""
    cursor.execute(statement,{'type':type})

def create_user_table(cursor):
    statement = """CREATE TABLE SITEUSER (
                USERID SERIAL PRIMARY KEY,
                USERNAME VARCHAR(20) UNIQUE NOT NULL,
                SALT VARCHAR(40) UNIQUE NOT NULL, 
                HASH VARCHAR(44) NOT NULL,
                EMAIL VARCHAR(40) NOT NULL,
                NAME VARCHAR(20) NOT NULL,
                SURNAME VARCHAR(20) NOT NULL,
                USERTYPEID INTEGER REFERENCES USERTYPE(ID) ON UPDATE CASCADE
                )"""
    cursor.execute(statement)

def getUserType(cursor,typename):
    statement = """SELECT ID FROM USERTYPE WHERE (TYPE = %(type)s)"""
    cursor.execute(statement,{'type':typename})

def getUser(cursor,username):
    statement = """SELECT SALT, HASH FROM SITEUSER WHERE (USERNAME = %(username)s)"""
    cursor.execute(statement, {'username':username});

def getAllUsers(cursor):
    statement = """SELECT ID,USERNAME,EMAIL,NAME,SURNAME,SALT,USERTYPEID FROM SITEUSER"""
    cursor.execute(statement);