class Book:
    def __init__(self, name, year, author_id, genre_id):
        self.name= name
        self.year=year
        self.author_id=author_id
        self.genre_id=genre_id


book1 = Book("The Sun Also Rises", 1926, 1, 1)
book2 = Book("Adventures of Hucleberry Finn", 1884, 2, 2)