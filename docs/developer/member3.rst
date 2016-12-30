Parts Implemented by Metehan GULTEKIN
=====================================
"BOOKS", "BOOKDETAILS", "GENRES, and "QUOTES" tables are created by me.

Books table:
   Columns:
      ID serial,

      TITLE varchar(40) not null,

      YEAR numeric(4) not null,

      AUTHORID integer references authors (id) on delete cascade,

      GENREID integer references genres (id) on delete cascade

   Constraints:
      PRIMARY KEY (id)

BookDetails table:
   Columns:
      ID serial,

      BOOKID integer references books (id) on delete cascase,

      IMGURL varchar(255) default ' ',

      DETAIL text default ' '

   Constraints:
      PRIMARY KEY (id)

Genres table:
   Columns:
      ID serial,

      NAME varchar(40) not null,

   Constraints:
      PRIMARY KEY (id)

Quotes table:
   Columns:
      QUOTEID serial,

      QUOTETEXT varchar(200) not null,

      YEAR numeric(4) not null,

      AUTHORID integer references authors (id) on delete cascade,

      BOOKID integer references books (id) on delete cascade

   Constraints:
      PRIMARY KEY (quoteid)

"Books", "Bookdetails", "Genres" and "Quotes" classes are created by me.::

   .. code-block:: Pyhton
   class Book:
    def __init__(self, id, title, year, author_id, genre_id):
        self.id = id
        self.title= title
        self.year=year
        self.author_id=author_id
        self.genre_id=genre_id

   class Bookdetails:
    def __init__(self, id, bookid, imgurl, detail):
        self.id = id
        self.bookid= bookid
        self.imgurl=imgurl
        self.detail=detail

   class Genre:
    def __init__(self,id,name):
        self.id = id
        self.name= name

   class Quote:
    def __init__(self, quoteid, quotetext, author_id, book_id):
        self.quoteid = quoteid
        self.quotetext = quotetext
        self.author_id = author_id
        self.book_id = book_id

I have worked in "Books.py", "Bookdetails.py", "Genres.py" and "Quotes.py" sources

Books.py
   Functions:
      insert_book
         For inserting a newly created book object into database
      selectBook
         For listing all the books in the database
      selectBookwithJoin
         For listing all the books in the database using join with other related tables in order to get a more detailed table
      selectBookbyID
         For selecting a single book from the database with its id
      selectBookbyIDwithJoin
         For selecting a single book from the database with its id using join with other related tables in order to get a more detailed table
      selectBookbyTitle
         For listing all the books with the same title
      selectBookbyYear
         For listing all the books published within the same year
      selectBookbyAuthor
         For listing all the books written by same author
      selectBookbyGenre
         For listing all the books of the same genre
      deleteBook
         For deleting a single book from database
      updateBook
         For updating a book that already exists in the database with new information

Bookdetails.py
   Functions:
      insert_book_details
         For inserting new details to an already created book
      get_book_imgurl
         For returning the cover photo url of a related book from the database
      get_book_detail
         For returning the details of a related book from the database
      update_book_details
         For updating the details of a book
      get_book_alldetails
         For listing all the books and all their details
      get_book_fulldetails
         For listing all the books and all their details using joins with other related tables in order to get a more detailed table
      get_book_fulldetails_byId
         For selecting a single book with its id and all its details
      get_book_alldetails_byId
         For selecting a single book with its id and all its details using joins with other related tables in order to get a more detailed table

Genres.py
   Functions:
      insert_genre
         For inserting a new genre into database
      selectGenre
         For listing all the genres from the database
      selectGenrebyName
         For listing all the genres with the same name from the database
      deleteGenre
         For deleting a single genre using its id
      updateGenre
         For updating an already existing genre with new information

Quotes.py
   Functions:
      insert_quote
         For inserting a new quote into database