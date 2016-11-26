import hashlib
import random
import crypt

class Message:
    def __init__(self, messageId, senderId, receiverId, text, isRead):
        self.messageId = messageId
        self.senderId = senderId
        self.receiverId = receiverId
        self.text = text
        self.isRead = isRead

def insertUserMessage(cursor,message):
    statement = """INSERT INTO USERMESSAGE (SENDERID, RECEIVERID, TEXT,ISREAD) VALUES (
                %(senderid)s, %(receiverid)s, %(text)s, %(isread)s
                )"""
    cursor.execute(statement,{'senderid':message.senderId,'receiverid':message.receiverId,'text':message.text, 'isread':str(message.isRead)});

def deleteUserMessage(cursor,messageid):
    statement = """DELETE FROM USERMESSAGE WHERE (MESSAGEID = %(messageid)s)"""
    cursor.execute(statement,{'messageid':messageid})
    
def changeMessageReadStatus(cursor,messageid, isread):
    statement = """UPDATE USERMESSAGE SET isRead=%(isread)s,
                WHERE (MESSAGEID = %(messageid)s)"""   
    cursor.execute(statement,{'messageid':messageid, 'isread':str(isread)})
                
def updateUserMessage(cursor,message):
    statement = """UPDATE USERMESSAGE SET SENDERID=%(senderid)s, 
                RECEIVERID=%(receiverid)s, TEXT=%(text)s, isRead=%(isread)s,
                WHERE (MESSAGEID = %(messageid)s)"""
    cursor.execute(statement,{'messageid':message.messageId,'senderid':message.senderId,'receiverid':message.receiverId,'text':message.text,'isread':str(isread)})

def getReceivedMessages(cursor,userid):
    statement = """SELECT MESSAGEID, SENDERID, RECEIVERID, TEXT, ISREAD, USERNAME AS SENDERUSERNAME FROM USERMESSAGE, SITEUSER 
                WHERE(RECEIVERID = %(receiverid)s
                AND SENDERID = SITEUSER.USERID)"""
    cursor.execute(statement,{'receiverid':userid})
    
def getSentMessages(cursor,userid):
    statement = """SELECT MESSAGEID, SENDERID, RECEIVERID, TEXT, ISREAD, USERNAME AS RECEIVERUSERNAME FROM USERMESSAGE, SITEUSER 
                WHERE(SENDERID = %(senderid)s
                AND RECEIVERID = SITEUSER.USERID)"""
    cursor.execute(statement,{'senderid':userid})             
                