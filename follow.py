import hashlib
import random
import crypt

class Follower:
    def __init__(self, followeruserid, followinguserid):
        self.followeruserid = followeruserid
        self.followinguserid = followinguserid

def follow(cursor,follow):
    statement = """INSERT INTO FOLLOWER (FOLLOWERUSERID, FOLLOWINGUSERID) VALUES (
                %(followeruserid)s, %(followinguserid)s
                )"""
    cursor.execute(statement,{'followeruserid':follow.followeruserid,'followinguserid':follow.followinguserid});

def unfollow(cursor,followinguserid, followeruserid):
    statement = """DELETE FROM FOLLOWER WHERE (FOLLOWINGUSERID = %(followinguserid)s) AND (FOLLOWERUSERID = %(followeruserid))"""
    cursor.execute(statement,{'followinguserid':followinguserid,'followeruserid':followeruserid})
                
def getUserFollowings(cursor,userid):
    statement = """SELECT FOLLOWINGUSERID,USERNAME AS FOLLOWINGUSERNAME, NAME AS FOLLOWINGNAME, SURNAME AS FOLLOWINGUSERSURNAME FROM FOLLOWER, SITEUSER 
                WHERE(FOLLOWERUSERID = %(followeruserid)s AND USERID = FOLLOWINGUSERID)"""
    cursor.execute(statement,{'followeruserid':userid})
    
def getUserFollowers(cursor,userid):
    statement = """SELECT FOLLOWERUSERID,USERNAME AS FOLLOWERUSERNAME, NAME AS FOLLOWERNAME, SURNAME AS FOLLOWERUSERSURNAME FROM FOLLOWER, SITEUSER 
                WHERE(FOLLOWINGUSERID = %(followinguserid)s AND USERID = FOLLOWERUSERID)"""
    cursor.execute(statement,{'followinguserid':userid})       
                