class News:
    def __init__(self, newstext, newsdate, newsheadline):
        self.newstext = newstext
        self.newsdate = newsdate
        self.newsheadline= newsheadline

def insert_news(cursor,news):
    statement = """INSERT INTO NEWS (NEWSTEXT,NEWSDATE,NEWSHEADLINE) VALUES (
                %s, %s, %s
                )"""
    cursor.execute(statement,(news.newstext,news.newsdate,news.newsheadline));
