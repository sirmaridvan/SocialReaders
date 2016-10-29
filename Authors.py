class Author:
    def __init__(self, name, lastname, birthdate, nationality, penname):
        self.name= name
        self.lastname=lastname
        self.birthdate=birthdate
        self.nationality=nationality
        self.penname = penname 
        
author1 = Author("Ernest","Hemingway",1899,"American",None)
author2 = Author("Samuel","Clemens",1835,"American","Mark Twain")