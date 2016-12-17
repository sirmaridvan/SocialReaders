import psycopg2 as dbapi2

class Author:
    def __init__(self,id, name, lastname, birthdate, nationality, penname,description,picture):
        self.id= id
        self.name= name
        self.lastname=lastname
        self.birthdate=birthdate
        self.nationality=nationality
        self.penname = penname
        self.description = description
        self.picture=picture

author1 = Author(None,"Ernest","Hemingway",1899,"American",None,None,"https://raw.githubusercontent.com/itucsdb1612/itucsdb1612/master/wiki_screenshots/sahalemre/Pic/hemingway.jpg")
author2 = Author(None,"Samuel","Clemens",1835,"American","Mark Twain",None,"https://raw.githubusercontent.com/itucsdb1612/itucsdb1612/master/wiki_screenshots/sahalemre/Pic/marktwain.jpg")
author3 = Author(None,"Metehan","Gültekin",1994,"Turkish",None,None,"https://raw.githubusercontent.com/itucsdb1612/itucsdb1612/master/wiki_screenshots/sahalemre/Pic/mete.jpg")
author4 = Author(None,"Ilay","Köksal",1995,"Turkish",None,None,"https://raw.githubusercontent.com/itucsdb1612/itucsdb1612/master/wiki_screenshots/sahalemre/Pic/ilay.jpg")

def insertAuthor(dsn,author):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ INSERT INTO AUTHORS (NAME, LASTNAME, BIRTHDATE, NATIONALITY, PENNAME, DESCRIPTION,PICTURE) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(statement,(author.name,author.lastname,author.birthdate,author.nationality,author.penname,author.description,author.picture))
        cursor.close()


def selectAuthor(dsn):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """SELECT * FROM AUTHORS ORDER BY ID ASC"""
        cursor.execute(statement)
        authors = cursor.fetchall()
        return authors
        cursor.close()


def selectAuthorbyLastName(dsn,lastname):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """SELECT * FROM AUTHORS WHERE LASTNAME = %s"""
        cursor.execute(statement,(lastname))
        authors = cursor.fetchall()
        return authors
        cursor.close()
        
        
def selectAuthorbyId(dsn,selectid):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """SELECT * FROM AUTHORS WHERE ID = %s"""
        cursor.execute(statement,[selectid])
        authors = cursor.fetchall()
        return authors
        cursor.close()        
        

def deleteAuthor(dsn,deleteid):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ DELETE FROM AUTHORS WHERE ID = %s"""
        cursor.execute(statement,(deleteid))
        cursor.close()

def updateAuthor(dsn,updateid,newauthor):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ UPDATE AUTHORS SET NAME = %s, LASTNAME = %s, BIRTHDATE = %s, NATIONALITY = %s, PENNAME = %s DESCRIPTION = %s PICTURE = %s WHERE ID = %s"""
        cursor.execute(statement,(newauthor.name,newauthor.lastname,newauthor.birthdate,newauthor.nationality,newauthor.penname,newauthor.description,newauthor.picture,updateid))
        cursor.close()
        
def getBooksofAuthor(dsn,authorid):
        with dbapi2.connect(dsn) as connection:
            cursor = connection.cursor()
            statement = """ SELECT TITLE FROM BOOKS WHERE AUTHORID = %s"""
            cursor.execute(statement,(authorid,))
            books = cursor.fetchall()
            cursor.close()
            return books