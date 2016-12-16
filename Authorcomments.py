import psycopg2 as dbapi2
 
 
class AuthorComment:
    def __init__(self,commenter,authorcommented,text):
        self.commenter = commenter
        self.authorcommented=authorcommented
        self.text= text
        
        
acomment1=AuthorComment(1,1," a test")
acomment2=AuthorComment(2,1," a add")

def selectauthorcomments(dsn,authorcommented):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ SELECT ID,USERNAME,COMMENT FROM AUTHORCOMMENTS,SITEUSER WHERE (AUTHORCOMMENTS.COMMENTER = SITEUSER.USERID) AND (AUTHORCOMMENTED = %s)"""
        cursor.execute(statement,(authorcommented,))
        comments = cursor.fetchall()
        return comments
        cursor.close()

def insertauthorcomment(dsn,comment):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ INSERT INTO AUTHORCOMMENTS (COMMENTER,AUTHORCOMMENTED,COMMENT) VALUES(%s,%s,%s)"""
        cursor.execute(statement,(comment.commenter,comment.authorcommented,comment.text))
        cursor.close()
    
def getauthorcommenterbycommentid(dsn,commentid):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement =""" SELECT COMMENTER FROM AUTHORCOMMENTS WHERE ID = %s """
        cursor.execute(statement,(commentid,))
        commenter = cursor.fetchone()
        return commenter
        cursor.close()

def  deleteauthorcommentbyid(dsn,commentid):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement =""" DELETE FROM AUTHORCOMMENTS WHERE ID = %s """
        cursor.execute(statement,(commentid,))
        cursor.close()