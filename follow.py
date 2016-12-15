import hashlib
import random
import crypt

class Follow:
    def __init__(self, followeruserid, followinguserid):
        self.followeruserid = followeruserid
        self.followinguserid = followinguserid

def follow(cursor,followeruserid,followinguserid):
    statement = """INSERT INTO FOLLOWER (FOLLOWERUSERID, FOLLOWINGUSERID) VALUES (
                %(followeruserid)s, %(followinguserid)s
                )"""
    cursor.execute(statement,{'followeruserid':followeruserid,'followinguserid':followinguserid});

def unfollow(cursor,followeruserid, followinguserid):
    statement = """DELETE FROM FOLLOWER WHERE (FOLLOWINGUSERID = %(followinguserid)s AND FOLLOWERUSERID = %(followeruserid)s)"""
    cursor.execute(statement,{'followinguserid':followinguserid,'followeruserid':followeruserid})
                
def getUserFollowings(cursor,userid):
    statement = """SELECT FOLLOWINGUSERID,USERNAME AS FOLLOWINGUSERNAME, NAME AS FOLLOWINGNAME, SURNAME AS FOLLOWINGUSERSURNAME FROM FOLLOWER, SITEUSER 
                WHERE(FOLLOWERUSERID = %(followeruserid)s AND USERID = FOLLOWINGUSERID)"""
    cursor.execute(statement,{'followeruserid':userid})
    
def getUserFollowers(cursor,userid):
    statement = """SELECT FOLLOWERUSERID,USERNAME AS FOLLOWERUSERNAME, NAME AS FOLLOWERNAME, SURNAME AS FOLLOWERUSERSURNAME FROM FOLLOWER, SITEUSER 
                WHERE(FOLLOWINGUSERID = %(followinguserid)s AND USERID = FOLLOWERUSERID)"""
    cursor.execute(statement,{'followinguserid':userid})       
                