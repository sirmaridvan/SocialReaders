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

def getUser(cursor,username):
    statement = """SELECT SALT, HASH FROM SITEUSER WHERE (USERNAME = %(username)s)"""
    cursor.execute(statement, {'username':username});