import psycopg2 as dbapi2
 
 
class Member:
    def __init__(self,groupuser,groupid):
        self.groupuser = groupuser
        self.groupid= groupid
    
    
def insert_member(dsn,memberid,groupid):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ INSERT INTO MEMBERS (GROUPUSER,GROUPID) VALUES (%s,%s)"""
        cursor.execute(statement,(memberid,groupid))
        cursor.close()