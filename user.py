import hashlib
import random
import crypt

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
    salt = crypt.mksalt(crypt.METHOD_SHA256)
    return salt[:40]

def createHash(salt,password):
    hash_object = hashlib.sha256(password.encode() + salt.encode())
    return hash_object.hexdigest()
    

def insert_usertype(cursor,type):
    statement = """INSERT INTO USERTYPE (TYPE) VALUES (
                %(type)s
                )"""
    cursor.execute(statement,{'type':type})
    
def insert_siteuser(cursor,user):
    statement = """INSERT INTO SITEUSER (USERNAME, SALT,HASH, EMAIL, NAME, SURNAME, USERTYPEID) VALUES (
                %s, %s, %s, %s, %s, %s, %s
                )"""
    cursor.execute(statement,(user.userName,user.salt, user.hash, user.email, 
                              user.name, user.surname, user.userTypeId));
                              
def getAllUserTypes(cursor):
    statement = """SELECT * FROM USERTYPE"""
    cursor.execute(statement)

def getUserType(cursor,typename):
    statement = """SELECT ID FROM USERTYPE WHERE (TYPE = %(type)s)"""
    cursor.execute(statement,{'type':typename})

def getUser(cursor,username):
    statement = """SELECT USERID, SALT, HASH, USERTYPEID FROM SITEUSER WHERE (USERNAME = %(username)s)"""
    cursor.execute(statement, {'username':username})

def getUserById(cursor,userid):
    statement = """SELECT * FROM SITEUSER WHERE (USERID = %(userid)s)"""
    cursor.execute(statement, {'userid':userid})

def getAllUsers(cursor):
    statement = """SELECT USERID,USERNAME,EMAIL,NAME,SURNAME,SALT,USERTYPEID FROM SITEUSER"""
    cursor.execute(statement)

def searchUsers(cursor, text):
    statement = """SELECT USERID,USERNAME,EMAIL,NAME,SURNAME,SALT,USERTYPEID FROM SITEUSER
                WHERE (USERNAME LIKE %%%(username)s%%)"""
    cursor.execute(statement, {'username':text})

def deleteUser(cursor,userid):
    statement = """DELETE FROM SITEUSER WHERE (USERID = %(userid)s)"""
    cursor.execute(statement,{'userid':userid})
    
def updateUser(cursor,user):
    statement = """UPDATE SITEUSER SET USERNAME=%(username)s, 
                EMAIL=%(email)s, NAME=%(name)s, SURNAME=%(surname)s,
                HASH=%(hash)s, USERTYPEID=%(usertypeid)s WHERE (USERID = %(userid)s)"""
    cursor.execute(statement,{'userid':user.userId,'username':user.userName,'email':user.email,'hash':user.hash,'name':user.name,'surname':user.surname,'usertypeid':user.userTypeId})
