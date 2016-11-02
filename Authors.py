import psycopg2 as dbapi2

class Author:
    def __init__(self,id, name, lastname, birthdate, nationality, penname):
        self.id= id
        self.name= name
        self.lastname=lastname
        self.birthdate=birthdate
        self.nationality=nationality
        self.penname = penname

author1 = Author(None,"Ernest","Hemingway",1899,"American",None)
author2 = Author(None,"Samuel","Clemens",1835,"American","Mark Twain")
author3 = Author(None,"Metehan","Gültekin",1995,"Turkish",None)
author4 = Author(None,"İlay","Köksal",1995,"Turkish",None)


def insertAuthor(dsn,author):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ INSERT INTO AUTHORS (NAME, LASTNAME, BIRTHDATE, NATIONALITY, PENNAME) VALUES (%s,%s,%s,%s,%s)"""
        cursor.execute(statement,(author.name,author.lastname,author.birthdate,author.nationality,author.penname))
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


def deleteAuthor(dsn,id):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ DELETE FROM AUTHORS WHERE ID = %s"""
        cursor.execute(statement,(id))
        cursor.close()

def updateAuthor(dsn,id,newauthor):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ UPDATE AUTHORS SET NAME = %s LASTNAME = %s BIRTHDAY = %s NATIONALITY = %s PENNAME = %s WHERE ID = %s"""
        cursor.execute(statement,(newauthor.name,newauthor.lastname,newauthor.birthdate,newauthor.nationality,newauthor.penname,id))
        cursor.close()