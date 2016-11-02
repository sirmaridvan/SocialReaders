class Genre:
    def __init__(self, genreid, genre_name):
        self.genreid = genreid
        self.genre_name = genre_name

def insert_genre(cursor, genre):
        statement = """INSERT INTO GENRES (GENRENAME) VALUES (
                %s
                )"""
        cursor.execute(statement,(genre.genre_name))

