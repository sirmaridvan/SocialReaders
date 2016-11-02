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

def select_newsdate(cursor):
        statement = """SELECT * FROM NEWS ORDER BY NEWSDATE ASC"""
        cursor.execute(statement)
        news = cursor.fetchall()
        return news
    
def select_newsheadline(cursor):
        statement = """SELECT * FROM NEWS ORDER BY NEWSHEADLINE ASC"""
        cursor.execute(statement)
        news = cursor.fetchall()
        return news
        
def delete_news(dsn,newsdate):
        statement = """ DELETE FROM NEWS WHERE NEWSDATE = %s"""
        cursor.execute(statement,(newsdate))
        
def update_news(cursor,newsheadline):
        statement = """ UPDATE NEWS SET NEWSTEXT = %s NEWSDATE = %s NEWSHEADLINE = %s WHERE NEWSHEADLINE = %s """
        cursor.execute(statement)