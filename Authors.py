class Author:
    def __init__(self, name, lastname, birthdate, nationality, penname):
        self.name= name
        self.lastname=lastname
        self.birthdate=birthdate
        self.nationality=nationality
        self.penname = penname

author1 = Author("Ernest","Hemingway",1899,"American",None)
author2 = Author("Samuel","Clemens",1835,"American","Mark Twain")


def insert_author(author):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ INSERT INTO AUTHORS (NAME, LASTNAME, BIRTHDATE, NATIONALITY, PENNAME) VALUES (%s,%s,%s,%s,%s)"""
        cursor.execute(statement,(author.name,author.lastname,author.birthdate,author.nationality,author.penname))
        cursor.close()


def selectAuthor():
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """SELECT * FROM AUTHORS ORDER BY ID ASC"""
        cursor.execute(statement)
        cursor.close()


def selectAuthorbyLastName(lastname):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """SELECT * FROM AUTHORS WHERE LASTNAME = %s"""
        cursor.execute(statement,(lastname))
        cursor.close()


def deleteAuthor(id):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ DELETE FROM AUTHORS WHERE ID = %s"""
        cursor.execute(statement,(id))
        cursor.close()

def updateAuthor(id,newauthor):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ UPDATE AUTHORS SET NAME = %s LASTNAME = %s BIRTHDAY = %s NATIONALITY = %s PENNAME = %s WHERE ID = %s"""
        cursor.execute(statement,(newauthor.name,newauthor.lastname,newauthor.birthdate,newauthor.nationality,newauthor.penname,id))
        cursor.close()