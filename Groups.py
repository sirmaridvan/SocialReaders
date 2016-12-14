import psycopg2 as dbapi2

class Group:
    def __init__(self,id,name):
        self.id = id
        self.name= name
        
group1 = Group(None,"databey")



def insert_group(dsn,group):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ INSERT INTO GROUPS (NAME) VALUES (%s)"""
        cursor.execute(statement,(group.name,))
        cursor.close()
        

def selectGroup(dsn):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """SELECT * FROM GROUPS ORDER BY ID ASC"""
        cursor.execute(statement)
        groups = cursor.fetchall()
        return groups
        cursor.close()

def selectGroupbyName(dsn,name):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """SELECT * FROM GROUPS WHERE NAME = %s"""
        cursor.execute(statement,(name,))
        groups = cursor.fetchall()
        return groups
        cursor.close()


def deleteGroup(dsn,id):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ DELETE FROM GROUPS WHERE ID = %s """
        cursor.execute(statement,(id,))
        cursor.close()

def updateGroup(dsn,id,newgroup):
    with dbapi2.connect(dsn) as connection:
        cursor = connection.cursor()
        statement = """ UPDATE GROUPS SET NAME = %s WHERE ID = %s"""
        cursor.execute(statement,(newgroup.name,id))
        cursor.close()