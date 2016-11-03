import psycopg2 as dbapi2

class Genre:
    def __init__(self,id,name):
        self.id = id
        self.name= name

def insert_genre(dsn,genre):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ INSERT INTO GENRES (NAME) VALUES (%s)"""
        cursor.execute(statement,(genre.name,))
        cursor.close()

def selectGenre(dsn):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """SELECT * FROM GENRES ORDER BY ID ASC"""
        cursor.execute(statement)
        genres = cursor.fetchall()
        return genres
        cursor.close()

def selectGenrebyName(dsn,name):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """SELECT * FROM GENRES WHERE NAME = %s"""
        cursor.execute(statement,(name))
        genres = cursor.fetchall()
        return genres
        cursor.close()

def deleteGenre(dsn,id):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ DELETE FROM GENRES WHERE ID = %s"""
        cursor.execute(statement,(id))
        cursor.close()

def updateGenre(dsn,id,newgenre):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ UPDATE GENRES SET NAME = %s WHERE ID = %s"""
        cursor.execute(statement,(newgenre.name,id))
        cursor.close()