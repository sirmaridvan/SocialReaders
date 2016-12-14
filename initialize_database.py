import psycopg2 as dbapi2


def drop_tables(cursor):
    statement = """
                DROP TABLE IF EXISTS BLOGS CASCADE;
                DROP TABLE IF EXISTS JOBS CASCADE;
                DROP TABLE IF EXISTS FEEDS CASCADE;
                DROP TABLE IF EXISTS FEEDTYPES CASCADE;
                DROP TABLE IF EXISTS NEWS CASCADE;
                DROP TABLE IF EXISTS S CASCADE;
                DROP TABLE IF EXISTS BOOKS CASCADE;
                DROP TABLE IF EXISTS QUOTES CASCADE;
                DROP TABLE IF EXISTS GENRES CASCADE;
                """
    cursor.execute(statement)

def dropgroupandauthortables(dsn):
        with dbapi2.connect(dsn) as connection:
            cursor = connection.cursor()
            statement = """ 
                DROP TABLE IF EXISTS GROUPS CASCADE;
                DROP TABLE IF EXISTS MEMBERS CASCADE;
                DROP TABLE IF EXISTS GROUPCOMMENTS CASCADE;
                DROP TABLE IF EXISTS AUTHORS CASCADE;
                """
            cursor.execute(statement)
            cursor.close()
    


##Elif's drop operations###

def dropUserTypeTable(cursor):
    statement = """
                DROP TABLE IF EXISTS USERTYPE CASCADE;
                """
    cursor.execute(statement)

def dropUserTable(cursor):
    statement = """
                DROP TABLE IF EXISTS SITEUSER CASCADE;
                """
    cursor.execute(statement)

def dropFollowerTable(cursor):
    statement = """
                DROP TABLE IF EXISTS FOLLOWER CASCADE;
                """
    cursor.execute(statement)

def dropUserMessagesTable(cursor):
    statement = """
                DROP TABLE IF EXISTS USERMESSAGE CASCADE;
                """
    cursor.execute(statement)

def create_blogs_table(cursor):
    statement = """CREATE TABLE IF NOT EXISTS BLOGS (
                ID SERIAL PRIMARY KEY ,
                USERID INTEGER REFERENCES SITEUSER (USERID),
                DATE DATE NOT NULL DEFAULT CURRENT_DATE,
                HEADER VARCHAR(20) NOT NULL,
                TEXT TEXT NOT NULL
                )"""
    cursor.execute(statement);

def create_jobs_table(cursor):
    statement = """CREATE TABLE IF NOT EXISTS JOBS (
                ID SERIAL PRIMARY KEY,
                USERID INTEGER REFERENCES SITEUSER (USERID),
                DATE DATE NOT NULL DEFAULT CURRENT_DATE,
                HEADER VARCHAR(20) NOT NULL,
                DESCRIPTION TEXT NOT NULL
                )"""
    cursor.execute(statement);


def create_feedtypes_table(cursor):
    statement = """CREATE TABLE IF NOT EXISTS FEEDTYPES (
                ID PRIMARY KEY,
                TYPE TEXT NOT NULL
                )"""
    cursor.execute(statement);

def create_feeds_table(cursor):
    statement = """CREATE TABLE IF NOT EXISTS FEEDS (
                ID SERIAL PRIMARY KEY,
                DATE DATE NOT NULL DEFAULT CURRENT_DATE,
                USERID INTEGER REFERENCES SITEUSER (USERID),
                BOOKID INTEGER REFERENCES BOOKS (BOOKID),
                TYPEID INTEGER REFERENCES FEEDTYPES (ID)
                )"""
    cursor.execute(statement);

def create_usertype_table(cursor):
    statement = """CREATE TABLE USERTYPE (
                ID SERIAL PRIMARY KEY,
                TYPE VARCHAR(8) NOT NULL
                )"""
    cursor.execute(statement);

def create_user_table(cursor):
    statement = """CREATE TABLE SITEUSER (
                USERID SERIAL PRIMARY KEY,
                USERNAME VARCHAR(20) UNIQUE NOT NULL,
                SALT VARCHAR(40) UNIQUE NOT NULL,
                HASH VARCHAR(64) NOT NULL,
                EMAIL VARCHAR(40) NOT NULL,
                NAME VARCHAR(20) NOT NULL,
                SURNAME VARCHAR(20) NOT NULL,
                USERTYPEID INTEGER REFERENCES USERTYPE(ID) ON DELETE RESTRICT ON UPDATE CASCADE
                )"""
    cursor.execute(statement)

def create_user_follower_table(cursor):
    statement = """CREATE TABLE FOLLOWER(
                FOLLOWERUSERID INTEGER REFERENCES SITEUSER(USERID) ON DELETE RESTRICT ON UPDATE CASCADE,
                FOLLOWINGUSERID INTEGER REFERENCES SITEUSER(USERID) ON DELETE RESTRICT ON UPDATE CASCADE,
                PRIMARY KEY(FOLLOWERUSERID,FOLLOWINGUSERID)
                )"""
    cursor.execute(statement)

def create_user_message_table(cursor):
    statement = """CREATE TABLE USERMESSAGE (
                MESSAGEID SERIAL PRIMARY KEY,
                SENDERID INTEGER REFERENCES SITEUSER(USERID) ON DELETE RESTRICT ON UPDATE CASCADE,
                RECEIVERID INTEGER REFERENCES SITEUSER(USERID) ON DELETE RESTRICT ON UPDATE CASCADE,
                TEXT VARCHAR(200) NOT NULL,
                ISREAD BOOLEAN NOT NULL
                )"""
    cursor.execute(statement)

''' Author table '''

def create_author_table(dsn):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ CREATE TABLE IF NOT EXISTS AUTHORS(
            ID SERIAL PRIMARY KEY,
            NAME VARCHAR(50) NOT NULL,
            LASTNAME VARCHAR(50) NOT NULL,
            BIRTHDATE NUMERIC(4) NOT NULL,
            NATIONALITY VARCHAR(50) NOT NULL,
            PENNAME VARCHAR(50),
            DESCRIPTION VARCHAR(255),
            PICTURE VARCHAR(255) 
        )"""
        cursor.execute(statement)
        cursor.close()


''' Groups Table '''

def create_groups_table(dsn):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ CREATE TABLE IF NOT EXISTS GROUPS (
            ID SERIAL PRIMARY KEY ,
            NAME VARCHAR(50) NOT NULL
        )"""
        cursor.execute(statement)
        cursor.close()

def create_genre_table(dsn):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ CREATE TABLE IF NOT EXISTS GENRES (
            ID SERIAL PRIMARY KEY,
            NAME VARCHAR(50) NOT NULL
        )"""
        cursor.execute(statement)
        cursor.close()


def create_members_table(dsn):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """CREATE TABLE IF NOT EXISTS MEMBERS (
            GROUPUSER INTEGER REFERENCES SITEUSER (USERID) ON DELETE CASCADE,
            GROUPID INTEGER REFERENCES GROUPS (ID) ON DELETE CASCADE
        )"""
        cursor.execute(statement)
        cursor.close()

def create_groupcomments_table(dsn):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """CREATE TABLE IF NOT EXISTS GROUPCOMMENTS (
            COMMENTID SERIAL PRIMARY KEY,
            COMMENTER INTEGER REFERENCES SITEUSER (USERID) ON DELETE CASCADE,
            GROUPCOMMENTED INTEGER REFERENCES GROUPS (ID) ON DELETE CASCADE,
            COMMENT VARCHAR(255)
        )"""
        cursor.execute(statement)
        cursor.close()


''' Book Table'''

def create_book_table(cursor):
    statement = """CREATE TABLE IF NOT EXISTS BOOKS (
                ID SERIAL PRIMARY KEY,
                TITLE VARCHAR(40) NOT NULL,
                YEAR NUMERIC(4) NOT NULL,
                AUTHORID INTEGER REFERENCES AUTHORS (ID),
                GENREID INTEGER REFERENCES GENRES (ID)
                )"""
    cursor.execute(statement)



''' Quote Table'''

def create_quote_table(cursor):
    statement = """CREATE TABLE IF NOT EXISTS QUOTES (
                QUOTEID SERIAL PRIMARY KEY,
                QUOTETEXT VARCHAR(200) NOT NULL,
                AUTHORID NUMERIC(4) NOT NULL,
                BOOKID NUMERIC(4) NOT NULL
                )"""
    cursor.execute(statement)



def create_news_table(cursor):
    statement = """CREATE TABLE IF NOT EXISTS NEWS (
                NEWSID SERIAL PRIMARY KEY,
                NEWSTEXT VARCHAR(200) NOT NULL,
                NEWSDATE NUMERIC(4) NOT NULL,
                NEWSHEADLINE VARCHAR(50) NOT NULL
                )"""
    cursor.execute(statement)


def insert_news(news):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ INSERT INTO NEWS (NEWSTEXT, NEWSDATE, NEWSHEADLINE) VALUES (%s, %s, %s)"""
        cursor.execute(statement,(news.newstext, news.newsdate,news.newsheadline))
        cursor.close()
