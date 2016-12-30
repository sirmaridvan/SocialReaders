Parts Implemented by Elif Benli
===============================
"SiteUser Table", "UserType Table", "Follower Table", "Event TAble" and "UserMessage Table" are created by me.

SiteUser Table
   Columns:
      USERID serial,
      
      USERNAME varchar(20) not null,
      
      SALT varchar(40) not null,
      
      HASH VARCHAR(64) not null,
      
      EMAIL VARCHAR(40) not null,
      
      NAME VARCHAR(20) not null,
      
      SURNAME VARCHAR(20) not null,
      
      USERTYPEID integer references usertype(id) on delete restrict on update cascade,
      
   Constraints:
      PRIMARY KEY(userid),
      
      UNIQUE(username, salt)

UserType Table
   Columns:
      ID serial,
      TYPE varchar(8) not null,
      
   Constraints:
      PRIMARY KEY(id)

Event Table
   Columns:
      FOLLOWERUSERID integer references siteuser(userid) on delete restrict on update cascade,
      
      FOLLOWINGUSERID integer references siteuser(userid) on delete restrict on update cascade,
      
   Constraints:
      PRIMARY KEY(followeruserid,followinguserid)

UserMessage Table
   Columns:
      MESSAGEID serial,
      
      SENDERID integer references siteuser(userid) on delete restrict on update cascade,
      
      RECEIVERID integer references siteuser(userid) on delete restrict on update cascade,
      
      TEXT varchar(80) not null,
      
      ISREAD boolean not null,
      
   Constraints:
      PRIMARY KEY(messageid)

Follower Table
   Columns:
      FOLLOWERUSERID integer references siteuser(userid) on delete restrict on update cascade,
      
      FOLLOWINGUSERID integer references siteuser(userid) on delete restrict on update cascade,
      
   Constraints:
      PRIMARY KEY(followeruserid, followinguserid)
      
"User", "Event", "Follow" and "Message" classes are created by me.::

   .. code-block:: Pyhton
      class User:
          def __init__(self, userId, userName, password, salt, hash, email, name, surname, userTypeId):
             self.userId = userId
             self.userName = userName
             self.password = password
             self.salt = salt
             self.hash = hash
             self.email = email
             self.name = name
             self.surname = surname
             self.userTypeId = userTypeId

      class Event:
          def __init__(self, eventid, eventdate, eventname, eventorganizer):
             self.eventid = eventid
             self.eventdate = eventdate
             self.eventname = eventname
             self.eventorganizer = eventorganizer 
      class Follow:
          def __init__(self, followeruserid, followinguserid):
             self.followeruserid = followeruserid
             self.followinguserid = followinguserid
      class Message:
           def __init__(self, messageId, senderId, receiverId, text, isRead):
             self.messageId = messageId
             self.senderId = senderId
             self.receiverId = receiverId
             self.text = text
             self.isRead = isRead
             
I have worked in "user.py", "event.py", "follow.py" and "message.py" sources

user.py
   Functions:
      createRandomSalt
         Used for creating a random salt
      createHash
         Used for creating a hash via composing of a password and randomly created salt
      inser_usertype
         Used for adding a user type in the usertype table
      insert_siteuser   
         Used for adding a user in the siteuser table
      getAllUserTypes
         Used for taking all existing usertypes
      getUserType
         Used for taking usertype id with given usertype
      getUser
         Used for taking an existing user with given username
      getUserById
         Used for taking an existing user with given userid
      getAllUsers
         Used for taking all existing users
      searchUsers
         Used for searching between users
      deleteUser
         Used for deleting an existing user in the siteuser table
      updateUser
         Used for updating an existing user in the siteuser table
follow.py
   Functions:
      follow
         Used for adding followers in the follower table
      isFollowing
         Used to control of follow operation for two user 
      unfollow
         Used to unfollow a user with given userids
      getUserFollowings
         Returns the followings of a user with given userid
      getUserFollowers
         Returns the followers of a user with given userid
message.py
   Functions:
      insertUserMessage
         Used for adding messages in the usermessage table
      deleteUserMessage
         User for deleting an existing message with given messageid in the usermessage table
      changeMessageReadStatus
         Used for updating whether a message is read
      updateUserMessage
         Used for updating an existing message
      getReceivedMessages
         Used for taking all received messages with given userid
      getSentMessages
         Used for taking all sent messages with given userid
      getMessage
         Used for taking an existing message with given messageid        
event.py
   Functions:
      insertEvent
         Used for adding events in the events table
      deleteEvent
         Used to delete event with given eventid in the event table
      getAllEvents
         Returns all of the events to be viewed in the event page from admin perspective
      getEventById
         Returns an event with given eventid
      getAllEventsWithStrMonth
         Returns all of the events with month
      updateEvent
         Used to change data of the event
    