import hashlib
import random
import crypt

class Event:
    def __init__(self, eventid, eventdate, eventname, eventorganizer):
        self.eventid = eventid
        self.eventdate = eventdate
        self.eventname = eventname
        self.eventorganizer = eventorganizer 

def insertEvent(cursor,event):
    statement = """INSERT INTO EVENT (EVENTDATE, EVENTNAME, EVENTORGANIZER) VALUES (
                to_date(%(eventdate)s,'DD/MM/YYYY'), %(eventname)s, %(eventorganizer)s
                )"""
    cursor.execute(statement,{'eventdate':event.eventdate, 'eventname':event.eventname, 'eventorganizer':event.eventorganizer});

def deleteEvent(cursor,eventid):
    statement = """DELETE FROM EVENT WHERE (EVENTID = %(eventid)s)"""
    cursor.execute(statement,{'eventid':eventid});
    
def getAllEvents(cursor):
    statement = """SELECT EVENTID, to_char(EVENTDATE,'DD/MM/YYYY'), EVENTNAME, EVENTORGANIZER FROM EVENT"""
    cursor.execute(statement);

def getEventById(cursor,eventid):
    statement = """SELECT EVENTID, to_char(EVENTDATE,'DD/MM/YYYY'), EVENTNAME, EVENTORGANIZER FROM EVENT WHERE (EVENTID = %(eventid)s)"""
    cursor.execute(statement, {'eventid':eventid})

def getAllEventsWithStrMonth(cursor):
    statement = """SELECT EVENTID, to_char(EVENTDATE,'DD/Mon/YYYY'), EVENTNAME, EVENTORGANIZER FROM EVENT"""
    cursor.execute(statement)

def updateEvent(cursor,event):
    statement = """UPDATE EVENT SET EVENTNAME=%(eventname)s, 
                EVENTDATE=to_date(%(eventdate)s,'DD/MM/YYYY'), EVENTORGANIZER=%(eventorganizer)s WHERE (EVENTID = %(eventid)s)"""
    cursor.execute(statement,{'eventid':event.eventid,'eventname':event.eventname,'eventdate':event.eventdate,'eventorganizer':event.eventorganizer})
