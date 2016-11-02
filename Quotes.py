class Quote:
    def __init__(self, quoteid, quotetext, author_id, book_id):
        self.quoteid = quoteid
        self.quotetext = quotetext
        self.author_id = author_id
        self.book_id = book_id

def insert_quote(cursor, quote):
        statement = """INSERT INTO QUOTES (QUOTETEXT,AUTHORID,BOOKID) VALUES (
                %s, %s, %s
                )"""
        cursor.execute(statement,(quote.quotetext, quote.author_id, quote.book_id))
