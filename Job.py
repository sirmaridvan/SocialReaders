import random

class Job:
    def __init__(self, id, date, header, description):
        self.id = id
        self.date=date
        self.header = header
        self.description = description

def insert_job(cursor,job):
    statement = """INSERT INTO JOBS (DATE,HEADER,DESCRIPTION) VALUES (
                %s, %s, %s
                )"""
    cursor.execute(statement,(job.date,job.header,job.description));