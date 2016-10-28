def drop_tables(cursor):
    statement = """
                DROP TABLE IF EXISTS SITEUSER CASCADE;
                DROP TABLE IF EXISTS USERTYPE CASCADE;
                """
    cursor.execute(statement)    
    
def create_usertype_table(cursor):
    statement = """CREATE TABLE USERTYPE (
                ID SERIAL PRIMARY KEY,
                TYPE VARCHAR(8) NOT NULL
                )"""
    cursor.execute(statement);

def insert_usertype(cursor,type):
    statement = """INSERT INTO USERTYPE (TYPE) VALUES (
                %(type)s
                )"""
    cursor.execute(statement,{'type':type})
    
def create_user_table(cursor):
    statement = """CREATE TABLE SITEUSER (
                USERID SERIAL PRIMARY KEY,
                USERNAME VARCHAR(20) UNIQUE NOT NULL,
                SALT VARCHAR(40) UNIQUE NOT NULL, 
                HASH VARCHAR(44) NOT NULL,
                EMAIL VARCHAR(20) NOT NULL,
                NAME VARCHAR(20) NOT NULL,
                SURNAME VARCHAR(20) NOT NULL,
                USERTYPEID INTEGER REFERENCES USERTYPE(ID) ON UPDATE CASCADE
                )"""
    cursor.execute(statement)
    
def insert_siteuser(cursor,user):
    statement = """INSERT INTO SITEUSER (USERNAME, SALT,HASH, EMAIL, NAME, SURNAME, USERTYPEID) VALUES (
                %s, %s, %s, %s, %s, %s, %s
                )"""
    cursor.execute(statement,(user.userName,user.salt, user.hash, user.email, 
                              user.name, user.surname, user.userTypeId));