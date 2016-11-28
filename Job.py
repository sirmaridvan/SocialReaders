class Job:
    def __init__(self, id, userId, date, header, description):
        self.id = id
        self.userId = userId
        self.date=date
        self.header = header
        self.description = description

def insertJob(cursor,job):
    statement = """INSERT INTO JOBS (USERID,DATE,HEADER,DESCRIPTION) VALUES (
                %s, %s, %s, %s
                )"""
    cursor.execute(statement,(job.userId,job.date,job.header,job.description));

def getJob(cursor,id):
    statement = """SELECT ID,USERNAME,DATE,HEADER,DESCRIPTION FROM JOBS,SITEUSER WHERE (JOBS.USERID=SITEUSER.USERID) AND (ID = %(id)s)"""
    cursor.execute(statement, {'id':id})

def getAllJobs(cursor):
    statement = """SELECT ID,USERNAME,DATE,HEADER,DESCRIPTION FROM JOBS,SITEUSER WHERE (JOBS.USERID=SITEUSER.USERID)"""
    cursor.execute(statement)
def deleteJob(cursor,id):
     statement = """DELETE FROM JOBS WHERE (ID = %(id)s)"""
     cursor.execute(statement,{'id':id})
def updateJob(cursor,header,description,id,date):
    statement = """UPDATE JOBS SET HEADER=%(header)s, DESCRIPTION=%(description)s, DATE=%(date)s WHERE (ID = %(id)s)"""
    cursor.execute(statement,{'header':header,'description':description,'date':date,'id':id})