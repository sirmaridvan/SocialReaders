import datetime
import os
import json
import ctypes  # An included library with Python install.
import re
import psycopg2 as dbapi2

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask.helpers import url_for

from initialize_database import *

from user import *
from Authors import *
from Books import *
from Genres import *
from Quotes import *
from BlogPost import *
from Job import *
from FeedType import *
from Feed import *
from flask.globals import session
from Groups import *
from News import *
from Members import *
from message import *
from Groupcomments import *

app = Flask(__name__)

@app.route('/dontrunthis')
def initialize():

    connection = dbapi2.connect(app.config['dsn'])
    try:
        cursor =connection.cursor()
        try:
            dropUserMessagesTable(cursor)
            dropUserTable(cursor)
            dropUserTypeTable(cursor)
            create_usertype_table(cursor)
            create_user_table(cursor)
            create_user_message_table(cursor)
            insert_usertype(cursor,'Admin')
            insert_usertype(cursor,'User')
            salt1 = createRandomSalt()
            password = '123456'
            createdHash = createHash(salt1,password)
            user1 = User(0,'benlielif',password,salt1,createdHash,'elfbnli@gmail.com','Elif','Benli',1)
            insert_siteuser(cursor,user1)
            salt2 = createRandomSalt()
            createdHash = createHash(salt2,password)
            user2 = User(0,'uyar',password,salt2,createdHash,'uyar@itu.edu.tr','Turgut','Uyar',1)
            insert_siteuser(cursor,user2)
        except dbapi2.Error as e:
            print(e.pgerror)
        finally:
            cursor.close()
    except dbapi2.Error as e:
        print(e.pgerror)
        connection.rollback()
    finally:
        connection.commit()
        connection.close()

    connection = dbapi2.connect(app.config['dsn'])
    try:
        cursor =connection.cursor()
        try:
            drop_tables(cursor)
            create_blogs_table(cursor)
            create_jobs_table(cursor)
            create_feeds_table(cursor)
            create_feedtypes_table(cursor)
            create_genre_table(app.config['dsn'])
            create_book_table(cursor)
            create_quote_table(cursor)
            create_news_table(cursor)
        except dbapi2.Error as e:
            print(e.pgerror)
        finally:
            cursor.close()
    except dbapi2.Error as e:
        print(e.pgerror)
        connection.rollback()
    finally:
        connection.commit()
        connection.close()


    create_groups_table(app.config['dsn'])
    insert_group(app.config['dsn'],group1)
    create_members_table(app.config['dsn'])
    create_author_table(app.config['dsn'])
    create_groupcomments_table(app.config['dsn'])
    insertAuthor(app.config['dsn'],author1)
    insertAuthor(app.config['dsn'],author2)
    insertAuthor(app.config['dsn'],author3)
    insertAuthor(app.config['dsn'],author4)
    insertcomment(app.config['dsn'],comment1)
    insertcomment(app.config['dsn'],comment2)

    connection = dbapi2.connect(app.config['dsn'])
    try:
        cursor =connection.cursor()
        try:
            newBest = News("Best authors are voted! There is also one Turkish in top 50",2016,"Best authers")
            #insert_news(news1)

            #insert_member(1,1)


            '''Creating and inserting samples for books, genres and quotes tables'''

            '''insert_genre function returns with "not all arguments converted during string formatting"
            needs to be resolved'''
            genre1 = Genre(0, "Novel")
            #insert_genre(cursor,genre1)
            genre2 = Genre(0, "Satire")
            #insert_genre(cursor,genre2)

            book1 = Book(0, "The Sun Also Rises", 1926, 1, 1)
            book2 = Book(0, "Adventures of Hucleberry Finn", 1884, 2, 2)

            insert_book(cursor, book1)
            insert_book(cursor, book2)

            quote1 = Quote(0, "you can't get away from yourself by moving from one place to another.", 1, 1)
            quote2 = Quote(0, "All right, then, I'll go to hell.", 2, 2)

            insert_quote(cursor, quote1)
            insert_quote(cursor, quote2)

            feedtype=FeedType(0,'adlı kitabı beğendi')
            insert_feedtype(cursor,feedtype)
            feedtype=FeedType(0,'adlı kitabı önerdi')
            insert_feedtype(cursor,feedtype)
            feedtype=FeedType(0,'adlı kitaba yorum yaptı')
            insert_feedtype(cursor,feedtype)

        except dbapi2.Error as e:
            print(e.pgerror)
        finally:
            cursor.close()
    except dbapi2.Error as e:
        print(e.pgerror)
        connection.rollback()
    finally:
        connection.commit()
        connection.close()

    logout()
    return redirect(url_for('home_page'))

#Ridvan's Part
##############

#Elif's Part
@app.route('/login',methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        connection = dbapi2.connect(app.config['dsn'])
        try:
            cursor =connection.cursor()
            try:
                error = None
                if "login-submit" in request.form:
                    username = request.form['username']
                    getUser(cursor, username)
                    if cursor.rowcount > 0:
                        ((userid,salt,hash,usertypeid),) =  cursor.fetchall()
                    else:
                        return render_template('login.html', isAlert = True, alertMessage = 'Username or password is invalid.')
                    password = request.form['password']
                    createdHash = createHash(salt,password)
                    if hash == createdHash:
                        session['logged_in'] = True
                        session['userId'] = userid
                        session['username'] = username
                        if usertypeid == 1:
                            session['isAdmin'] = True
                        else:
                            session['isAdmin'] = False
                        return redirect(url_for('home_page'))
                    else:
                        return render_template('login.html', isAlert = True, alertMessage = 'Username or password is invalid.')

                elif "register-submit" in request.form:
                    salt = createRandomSalt()
                    getUserType(cursor,'User')
                    ((typeid),) = cursor.fetchall()
                    if request.form['password'] == request.form['confirm-password']:
                        insert_siteuser(cursor,User(0,request.form['username'], request.form['password'], salt, createHash(salt,request.form['password']),request.form['email'],request.form['name'],request.form['surname'],typeid))
                        return redirect(url_for('home_page'))
                    else:
                        return render_template('login.html', isAlert = True, alertMessage = 'Passwords mismatched.')
            except dbapi2.Error as e:
                print(e.pgerror)
            finally:
                cursor.close()
        except dbapi2.Error as e:
            print(e.pgerror)
            connection.rollback()
        finally:
            connection.commit()
            connection.close()
    elif 'logged_in' in session and session['logged_in'] == True:
        return redirect(url_for('home_page'))
    else:
        return render_template('login.html',isAlert = False, alertMessage = '')

@app.route('/logout')
def logout_page():
    if 'logged_in' in session and session['logged_in'] == True:
        session['logged_in'] = False
        session['isAdmin'] = False
        session['username'] = ''
        session['userId'] = 0
    return redirect(url_for('home_page'))

@app.route('/profile', methods=['GET', 'POST'])
def profile_page():
    if 'logged_in' in session and session['logged_in'] == True:
        connection = dbapi2.connect(app.config['dsn'])
        try:
            cursor =connection.cursor()
            try:
                getReceivedMessages(cursor,session['userId'])
                if cursor.rowcount > 9:
                    messageCount = '9+'
                else:
                    messageCount = str(cursor.rowcount)
                return render_template('profile.html', unreadMessageCount = messageCount)
            except dbapi2.Error as e:
                print(e.pgerror)
            finally:
                cursor.close()
        except dbapi2.Error as e:
            print(e.pgerror)
            connection.rollback()
        finally:
            connection.commit()
            connection.close()
    else:
        return redirect(url_for('home_page'))

@app.route('/admin/users',methods=['GET', 'POST'])
def users_page():
    if 'logged_in' in session and session['logged_in'] == True and session['isAdmin'] == True:
        connection = dbapi2.connect(app.config['dsn'])
        try:
            cursor =connection.cursor()
            try:
                if request.method == 'POST':
                    if "edit" in request.form:
                        userid = request.form['editid']

                    elif "delete" in request.form:
                        userid = request.form['deleteid']
                        deleteUser(cursor,str(userid))
                    getAllUsers(cursor)
                    mUsers = cursor.fetchall()
                    return render_template('users.html',users=mUsers)
                else:
                    getAllUsers(cursor)
                    mUsers = cursor.fetchall()
                    return render_template('users.html',users=mUsers)
            except dbapi2.Error as e:
                print(e.pgerror)
            finally:
                cursor.close()
        except dbapi2.Error as e:
            print(e.pgerror)
            connection.rollback()
        finally:
            connection.commit()
            connection.close()
    else:
        return redirect(url_for('home_page'))

@app.route('/admin/useradd',methods=['GET', 'POST'])
def userAdd_page():
    if 'logged_in' in session and session['logged_in'] == True and session['isAdmin'] == True:
        connection = dbapi2.connect(app.config['dsn'])
        try:
            cursor =connection.cursor()
            try:
                if request.method == 'POST':
                    if "add" in request.form:
                        salt = createRandomSalt()
                        hash = createHash(salt,request.form['password'])
                        user = User(0,request.form['username'],request.form['password'],salt,hash,request.form['email'],request.form['name'],request.form['surname'],request.form['usertypeid'])
                        insert_siteuser(cursor,user)
                        return redirect(url_for('users_page'))
                else:
                    getAllUserTypes(cursor)
                    mUserTypes = cursor.fetchall()
                    return render_template('useradd.html',userTypes = mUserTypes)
            except dbapi2.Error as e:
                    print(e.pgerror)
            finally:
                    cursor.close()
        except dbapi2.Error as e:
            print(e.pgerror)
            connection.rollback()
        finally:
            connection.commit()
            connection.close()
    else:
        return redirect(url_for('home_page'))

@app.route('/admin/userupdate',methods=['GET', 'POST'])
def userUpdate_page():
    if 'logged_in' in session and session['logged_in'] == True and session['isAdmin'] == True:
        connection = dbapi2.connect(app.config['dsn'])
        try:
            cursor =connection.cursor()
            try:
                if request.method == 'GET':
                    userid = request.args.get('id')
                    getUserById(cursor,userid)
                    ((id,username,salt,hash,email,name,surname,usertypeid),) = cursor.fetchall()
                    mUser = User(id,username,"",salt,hash,email,name,surname,usertypeid)
                    getAllUserTypes(cursor)
                    mUserTypes = cursor.fetchall()
                    return render_template('userupdate.html',user = mUser, userTypes = mUserTypes)
                elif request.method == 'POST':
                    if 'update' in request.form:
                        user = User(request.form['userid'],request.form['username'],request.form['password'],request.form['salt'],createHash(request.form['salt'],request.form['password']), request.form['email'],request.form['name'],request.form['surname'],request.form['usertypeid'])
                        updateUser(cursor,user)
                    return redirect(url_for('users_page'))
            except dbapi2.Error as e:
                    print(e.pgerror)
            finally:
                    cursor.close()
        except dbapi2.Error as e:
            print(e.pgerror)
            connection.rollback()
        finally:
            connection.commit()
            connection.close()
        return render_template('userupdate.html')
    else:
        return redirect(url_for('home_page'))

@app.route('/messages',methods=['GET', 'POST'])
def messages_page():
    if 'logged_in' in session and session['logged_in'] == True:
        if request.method == 'GET':
            connection = dbapi2.connect(app.config['dsn'])
            try:
                cursor =connection.cursor()
                try:
                    getReceivedMessages(cursor,session['userId'])
                    mReceivedMessages = cursor.fetchall()

                    getSentMessages(cursor,session['userId'])
                    mSentMessages = cursor.fetchall()
                    return render_template('messages.html',isAlert = False, alertMessage = '',receivedMessages = mReceivedMessages, sentMessages = mSentMessages)
                except dbapi2.Error as e:
                        print(e.pgerror)
                finally:
                        cursor.close()
            except dbapi2.Error as e:
                print(e.pgerror)
                connection.rollback()
            finally:
                connection.commit()
                connection.close()
            return render_template('messages.html')
        elif 'sendMessage' in request.form:
            connection = dbapi2.connect(app.config['dsn'])
            try:
                cursor =connection.cursor()
                try:
                    getUser(cursor,request.form['receiverUserName'])
                    if cursor.rowcount > 0:
                        ((receiver),) = cursor.fetchall()
                        message = Message(0,session['userId'],receiver[0],request.form['message'],False)
                        insertUserMessage(cursor,message)
                        getReceivedMessages(cursor,session['userId'])
                        mReceivedMessages = cursor.fetchall()
                        getSentMessages(cursor,session['userId'])
                        mSentMessages = cursor.fetchall()
                        return render_template('messages.html',isAlert = False, alertMessage = '',receivedMessages = mReceivedMessages, sentMessages = mSentMessages)
                    else:
                        getReceivedMessages(cursor,session['userId'])
                        mReceivedMessages = cursor.fetchall()

                        getSentMessages(cursor,session['userId'])
                        mSentMessages = cursor.fetchall()
                        return render_template('messages.html', isAlert = True, alertMessage = 'Could not find specified user.',receivedMessages = mReceivedMessages, sentMessages = mSentMessages)
                except dbapi2.Error as e:
                        print(e.pgerror)
                finally:
                        cursor.close()
            except dbapi2.Error as e:
                print(e.pgerror)
                connection.rollback()
            finally:
                connection.commit()
                connection.close()
            return render_template('messages.html')
        elif 'delete' in request.form:
            connection = dbapi2.connect(app.config['dsn'])
            try:
                cursor =connection.cursor()
                try:
                    messageId = request.form['mid']

                    deleteUserMessage(cursor,messageId)

                    getReceivedMessages(cursor,session['userId'])
                    mReceivedMessages = cursor.fetchall()

                    getSentMessages(cursor,session['userId'])
                    mSentMessages = cursor.fetchall()
                    return render_template('messages.html', isAlert = False, alertMessage = '',receivedMessages = mReceivedMessages, sentMessages = mSentMessages)
                except dbapi2.Error as e:
                        print(e.pgerror)
                finally:
                        cursor.close()
            except dbapi2.Error as e:
                print(e.pgerror)
                connection.rollback()
            finally:
                connection.commit()
                connection.close()
            return render_template('messages.html')
    else:
        return redirect(url_for('home_page'))
##############

#Emre's Part
##############

#Metehan's Part
##############

#Omer's Part
##############

@app.route('/')
def home_page():
    if 'logged_in' in session and session['logged_in'] == True:
        now = datetime.datetime.now()
        return render_template('home.html', current_time=now.ctime())
    else:
        ##Kullanici giris yapmamis. Burada baska tipte bir anasayfa olacak
        now = datetime.datetime.now()
        return render_template('home.html', current_time=now.ctime())
@app.route('/jobs', methods=['GET', 'POST'])
def jobs_page():
    if 'logged_in' in session and session['logged_in'] == True and session['isAdmin'] == True:
        connection = dbapi2.connect(app.config['dsn'])
        try:
            cursor =connection.cursor()
            try:
                if request.method == 'GET':
                    getAllJobs(cursor)
                    return render_template('jobs.html', jobs = cursor)
                if request.method == 'POST':
                    if "delete" in request.form:
                        id = request.form['deleteid']
                        deleteJob(cursor,id)
                        return redirect(url_for('jobs_page'))
            except dbapi2.Error as e:
                print(e.pgerror)
            finally:
                cursor.close()
        except dbapi2.Error as e:
            print(e.pgerror)
            connection.rollback()
        finally:
            connection.commit()
            connection.close()
        return render_template('jobs.html')
    else:
        return redirect(url_for('home_page'))
@app.route('/describeJob', methods=['GET', 'POST'])
def describe_job_page():
    if 'logged_in' in session and session['logged_in'] == True and session['isAdmin'] == True:
        if request.method == 'POST':
            if "submit" in request.form:
                userId=session['userId']
                date=datetime.datetime.now()
                header=request.form['header']
                description = request.form['description']
                job = Job(0,userId,datetime.date.today(),header,description);
                connection = dbapi2.connect(app.config['dsn'])
                try:
                    cursor =connection.cursor()
                    try:
                      insertJob(cursor,job)
                    except dbapi2.Error as e:
                        print(e.pgerror)
                    finally:
                        cursor.close()
                except dbapi2.Error as e:
                    print(e.pgerror)
                    connection.rollback()
                finally:
                    connection.commit()
                    connection.close()
                return redirect(url_for('jobs_page'))
        return render_template('describeJob.html')
    else:
        return redirect(url_for('home_page'))
@app.route('/updateJob', methods=['GET', 'POST'])
def update_job_page():
    if 'logged_in' in session and session['logged_in'] == True and session['isAdmin'] == True:
        connection = dbapi2.connect(app.config['dsn'])
        try:
            cursor =connection.cursor()
            try:
                if request.method == 'GET':
                    userid = request.args.get('userid')
                    statement = """SELECT ID, HEADER,DESCRIPTION FROM JOBS WHERE (ID=%(userid)s)"""
                    cursor.execute(statement,{'userid':userid})
                    return render_template('updateJob.html',job=cursor)
                if request.method == 'POST':
                    updateJob(cursor,request.form['header'],request.form['description'],request.form['userid'],datetime.datetime.now())
                    return redirect(url_for('jobs_page'))
            except dbapi2.Error as e:
                print(e.pgerror)
            finally:
                cursor.close()
        except dbapi2.Error as e:
            print(e.pgerror)
            connection.rollback()
        finally:
            connection.commit()
            connection.close()

        return render_template('updateJob.html')
    else:
        redirect(url_for('home_page'))

@app.route('/updatePost', methods=['GET', 'POST'])
def update_post_page():
    if 'logged_in' in session and session['logged_in'] == True:
        connection = dbapi2.connect(app.config['dsn'])
        try:
            cursor =connection.cursor()
            try:
                if request.method == 'GET':
                    userid = request.args.get('userid')
                    if session['userId']==int(userid):
                        id = request.args.get('id')
                        statement = """SELECT ID, HEADER,TEXT FROM BLOGS WHERE (ID=%(id)s)"""
                        cursor.execute(statement,{'id':id})
                        return render_template('updatePost.html',post=cursor)
                    else:
                        return redirect(url_for('blogs_page'))
                if request.method == 'POST':
                    updatePost(cursor,request.form['text'],request.form['userid'],datetime.datetime.now())
                    return redirect(url_for('blogs_page'))
            except dbapi2.Error as e:
                print(e.pgerror)
            finally:
                cursor.close()
        except dbapi2.Error as e:
            print(e.pgerror)
            connection.rollback()
        finally:
            connection.commit()
            connection.close()

        return render_template('updatePost.html')
    else:
        redirect(url_for('home_page'))

@app.route('/blogs', methods=['GET', 'POST'])
def blogs_page():
    if 'logged_in' in session and session['logged_in'] == True:
        connection = dbapi2.connect(app.config['dsn'])
        try:
            cursor =connection.cursor()
            try:
                if request.method == 'GET':
                    getAllPosts(cursor)
                    return render_template('blogs.html', blogs = cursor)
                if request.method == 'POST':
                    if "delete" in request.form:
                        id = request.form['deleteid']
                        userid = request.form['userid']
                        if session['userId']==int(userid):
                            deletePost(cursor,id)
                            return redirect(url_for('blogs_page'))
                        else:
                            return redirect(url_for('blogs_page'))
            except dbapi2.Error as e:
                print(e.pgerror)
            finally:
                cursor.close()
        except dbapi2.Error as e:
            print(e.pgerror)
            connection.rollback()
        finally:
            connection.commit()
            connection.close()
        return render_template('blogs.html')
    else:
        return redirect(url_for('home_page'))

@app.route('/writepost', methods=['GET', 'POST'])
def write_post_page():
    if 'logged_in' in session and session['logged_in'] == True:
        if request.method == 'POST':
            if "submit" in request.form:

                userId=session['userId']
                date=datetime.datetime.now()
                header="header"
                text = request.form['text']
                blogPost = BlogPost(0,userId,datetime.date.today(),header,text);
                connection = dbapi2.connect(app.config['dsn'])
                try:
                    cursor =connection.cursor()
                    try:
                      insert_blogPost(cursor,blogPost)
                    except dbapi2.Error as e:
                        print(e.pgerror)
                    finally:
                        cursor.close()
                except dbapi2.Error as e:
                    print(e.pgerror)
                    connection.rollback()
                finally:
                    connection.commit()
                    connection.close()
                return redirect(url_for('blogs_page'))
        return render_template('writePost.html')
    else:
        return redirect(url_for('home_page'))
##########ADMIN PAGES##########

@app.route('/admin')
def admin_index():
    ##bu admin sayfasi oldugu icin kullanici admin mi diye kontrol etmek lazim
    if 'logged_in' in session and session['logged_in'] == True and session['isAdmin'] == True:
        return render_template('admin_index.html')
    else:
        return redirect(url_for('home_page'))
###############################




@app.route('/admin/authors',methods=['GET', 'POST'])
def authoradmin_page():
    if 'logged_in' in session and session['logged_in'] == True and session['isAdmin'] == True:
        if request.method == 'GET':
            return render_template('authoradmin.html',authors = selectAuthor(app.config['dsn']))
        else:
            if 'Delete' in request.form:
                deleteid = request.form['deleteid']
                deleteAuthor(app.config['dsn'],deleteid)
                return redirect(url_for('authoradmin_page'))
            if  'Update' in request.form:
                updateid = request.form['updateid']
                return render_template('authorupdate.html')

    else:
        return render_template('home_page.html')



@app.route('/admin/authorsAdd',methods=['GET', 'POST'])
def authorAdd_page():
    if 'logged_in' in session and session['logged_in'] == True and session['isAdmin'] == True:
        if request.method == 'GET':
            return render_template('authoradd.html')
        else:
            if 'Add' in request.form:
                name = request.form['name']
                lastname = request.form['lastname']
                birthyear = request.form['birthyear']
                nationality = request.form['nationality']
                penname = request.form['penname']
                newauthor = Author(None,name,lastname,birthyear,nationality,penname)
                insertAuthor(app.config['dsn'],newauthor)
                return redirect(url_for('authoradmin_page'))
        return render_template('authoradd.html')
    else:
        return render_template('home_page.html')



@app.route('/admin/authorsUpdate',methods=['GET', 'POST'])
def authorupdate_page():
    if 'logged_in' in session and session['logged_in'] == True and session['isAdmin'] == True:
        if request.method == 'GET':
            updateid = request.args.get('updateid')
            return render_template('authorupdate.html',updateauthor = selectAuthorbyId(app.config['dsn'],updateid))
        else:
            if 'Update' in request.form:
                updateid = request.form['updateid']
                name = request.form['name']
                lastname = request.form['lastname']
                birthyear = request.form['birthyear']
                nationality = request.form['nationality']
                penname = request.form['penname']
                updateauthor = Author(None,name,lastname,birthyear,nationality,penname)
                updateAuthor(app.config['dsn'],updateid,updateauthor)
                return redirect(url_for('authoradmin_page'))
            return render_template('authorupdate.html',updateauthor = selectAuthorbyId(app.config['dsn'],updateid))
    else:
        return render_template('home_page.html')

		
@app.route('/news',methods=['GET', 'POST'])
def news_page():
    if 'logged_in' in session and session['logged_in'] == True and session['isAdmin'] == True:
        connection = dbapi2.connect(app.config['dsn'])
        try:
            cursor =connection.cursor()
            try:
                if request.method == 'GET':
                    select_newsdate(cursor)
                    return render_template('news.html', news = cursor)
                if request.method == 'POST':
                    if "delete" in request.form:
                        id = request.form['deleteid']
                        delete_news(cursor,id)
                        return redirect(url_for('news_page'))
            except dbapi2.Error as e:
                print(e.pgerror)
            finally:
                cursor.close()
        except dbapi2.Error as e:
            print(e.pgerror)
            connection.rollback()
        finally:
            connection.commit()
            connection.close()
        return render_template('news.html')
    else:
        return redirect(url_for('home_page'))
@app.route('/newsAdd',methods=['GET', 'POST'])
def newsadd_page():
    if 'logged_in' in session and session['logged_in'] == True and session['isAdmin'] == True:
        if request.method == 'GET':
            return render_template('newsadd.html')
        else:
            if 'Add' in request.form:
                newsheadline = request.form['headline']
                newstext = request.form['text']
                newsdate = request.form['date']
                newnews = News(newstext,newsdate,newsheadline)
                insert_news(app.config['dsn'],newnews)
                return redirect(url_for('newsadmin_page'))
        return render_template('newsadd.html')
    else:
        return render_template('home_page.html')

@app.route('/updatenews', methods=['GET', 'POST'])
def update_news_page():
    if 'logged_in' in session and session['logged_in'] == True and session['isAdmin'] == True:
        connection = dbapi2.connect(app.config['dsn'])
        try:
            cursor =connection.cursor()
            try:
                if request.method == 'GET':
                    newsdate = request.args.get('newsheadline')
                    statement = """SELECT * FROM NEWS WHERE (newsdate=%(newsdate)s)"""
                    cursor.execute(statement,{'newsheadline':newsheadline})
                    return render_template('updatenews.html',news=cursor)
                if request.method == 'POST':
                    return redirect(url_for('jobs_page'))
            except dbapi2.Error as e:
                print(e.pgerror)
            finally:
                cursor.close()
        except dbapi2.Error as e:
            print(e.pgerror)
            connection.rollback()
        finally:
            connection.commit()
            connection.close()

        return render_template('updateJob.html')
    else:
        redirect(url_for('home_page'))



@app.route('/authors',methods=['GET', 'POST'])
def authors_page():
    if 'logged_in' in session and session['logged_in'] == True:
        if request.method == 'GET':
            return render_template('authors.html', authors = selectAuthor(app.config['dsn']))
    else:
        return redirect(url_for('home_page'))



@app.route('/groups',methods=['GET', 'POST'])
def groups_page():
    if 'logged_in' in session and session['logged_in'] == True:
        if request.method == 'GET':
            return render_template('groups.html',groups = selectGroup(app.config['dsn']))
        else:
            if 'Add' in request.form:
                name = request.form['groupname']
                group = Group(None,name)
                insert_group(app.config['dsn'],group)
                return render_template('groups.html',groups = selectGroup(app.config['dsn']))
            if 'Delete' in request.form:
                id=request.form['id']
                deleteGroup(app.config['dsn'],id)
                return render_template('groups.html',groups = selectGroup(app.config['dsn']))
            if 'Update' in request.form:
                id=request.form['id']
                newname = request.form['newname']
                newgroup = Group(id,newname)
                updateGroup(app.config['dsn'],id,newgroup)
                return render_template('groups.html',groups = selectGroup(app.config['dsn']))
            if 'Join' in request.form:
                groupid=request.form['id']
                memberid = session['userId']
                members = selectMember(app.config['dsn'],memberid,groupid)
                if members is None:
                    insert_member(app.config['dsn'],memberid,groupid)
                return render_template('groups.html',groups = selectGroup(app.config['dsn']))
            if 'Visit' in request.form:
                groupid=request.form['id']
                session["group"] = groupid
                return redirect(url_for('grouppage_page'));

    else:
        return redirect(url_for('home_page'))

@app.route('/grouppage',methods=['GET', 'POST'])
def grouppage_page():
    if 'logged_in' in session and session['logged_in'] == True:
        groupid = session["group"];
        return render_template('grouppage.html',comments = selectcomments(app.config['dsn'],groupid),membernames = getmembersbyjoin(app.config['dsn'],groupid))
    else:
        return redirect(url_for('home_page'))



@app.route('/genres',methods=['GET', 'POST'])
def genres_page():
    if 'logged_in' in session and session['logged_in'] == True:
        if request.method == 'GET':
            return render_template('genres.html',groups = selectGenre(app.config['dsn']))
        else:
            if 'Add' in request.form:
                name = request.form['genrename']
                genre = Genre(None,name)
                insert_genre(app.config['dsn'],genre)
                return render_template('genres.html',genres = selectGenre(app.config['dsn']))
            if 'Delete' in request.form:
                id=request.form['id']
                deleteGenre(app.config['dsn'],id)
                return render_template('genres.html',genres = selectGenre(app.config['dsn']))
            if 'Update' in request.form:
                id=request.form['id']
                newname = request.form['newname']
                newgenre = Genre(id,newname)
                updateGenre(app.config['dsn'],id,newgenre)
                return render_template('genres.html',genres = selectGenre(app.config['dsn']))
    else:
        return redirect(url_for('home_page'))


@app.route('/bookpage')
def book_page():
    if 'logged_in' in session and session['logged_in'] == True:
        return render_template('bookpage.html')
    else:
        return redirect(url_for('home_page'))



@app.route('/admin/books',methods=['GET', 'POST'])
def books_page():
    if 'logged_in' in session and session['logged_in'] == True and session['isAdmin'] == True:
        connection = dbapi2.connect(app.config['dsn'])
        try:
            cursor =connection.cursor()
            try:
                if request.method == 'POST':
                    if "edit" in request.form:
                        bookid = request.form['editid']

                    elif "delete" in request.form:
                        bookid = request.form['deleteid']
                        delete_book(cursor,bookid)
                    select_books(cursor)
                    mBooks = cursor.fetchall()
                    return render_template('bookadmin.html',books=mBooks)
                else:
                    select_books(cursor)
                    mBooks = cursor.fetchall()
                    return render_template('bookadmin.html',books=mBooks)
            except dbapi2.Error as e:
                print(e.pgerror)
            finally:
                cursor.close()
        except dbapi2.Error as e:
            print(e.pgerror)
            connection.rollback()
        finally:
            connection.commit()
            connection.close()
    else:
        return redirect(url_for('home_page'))
@app.route('/admin/bookadd',methods=['GET', 'POST'])
def bookAdd_page():
    if 'logged_in' in session and session['logged_in'] == True and session['isAdmin'] == True:
        connection = dbapi2.connect(app.config['dsn'])
        try:
            cursor =connection.cursor()
            try:
                if request.method == 'POST':
                    if "add" in request.form:
                        book = Book(0,request.form['title'],request.form['year'],request.form['author_id'],request.form['genre_id'])
                        insert_book(cursor,book)
                        return redirect(url_for('books_page'))
            except dbapi2.Error as e:
                    print(e.pgerror)
            finally:
                    cursor.close()
        except dbapi2.Error as e:
            print(e.pgerror)
            connection.rollback()
        finally:
            connection.commit()
            connection.close()
        return render_template('bookadd.html')
    else:
        return redirect(url_for('home_page'))
@app.route('/admin/bookupdate',methods=['GET', 'POST'])
def bookUpdate_page():
    if 'logged_in' in session and session['logged_in'] == True and session['isAdmin'] == True:
        connection = dbapi2.connect(app.config['dsn'])
        try:
            cursor =connection.cursor()
            try:
                if request.method == 'GET':
                    bookid = request.args.get('id')
                    select_bookid(cursor,bookid)
                    ((bookid, title, year, author_id, genre_id),) = cursor.fetchall()
                    mBook = Book(bookid,title,year, author_id, genre_id)
                    return render_template('bookupdate.html',book = mBook)
                elif request.method == 'POST':
                    if 'update' in request.form:
                        book = book(request.form['bookid'],request.form['title'],request.form['year'],request.form['author_id'],request.form['genre_id'])
                        update_book(cursor,book)
                    return redirect(url_for('books_page'))
            except dbapi2.Error as e:
                    print(e.pgerror)
            finally:
                    cursor.close()
        except dbapi2.Error as e:
            print(e.pgerror)
            connection.rollback()
        finally:
            connection.commit()
            connection.close()
        return render_template('bookupdate.html')
    else:
        return redirect(url_for('home_page'))

def logout():
    session['logged_in'] = False;
    session['username'] = "";
    session['isAdmin'] = False;

def get_elephantsql_dsn(vcap_services):
    """Returns the data source name for ElephantSQL."""
    parsed = json.loads(vcap_services)
    uri = parsed["elephantsql"][0]["credentials"]["uri"]
    match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
    user, password, host, _, port, dbname = match.groups()
    dsn = """user='{}' password='{}' host='{}' port={}
             dbname='{}'""".format(user, password, host, port, dbname)
    return dsn

# set the secret key.  keep this really secret:
app.secret_key = '+_9o$w9+9xro!-y(wvuv+vvyc!$x(@ak(!oh@ih0ul%+6cf=$f'

if __name__ == '__main__':
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5000, True
    #This part is logins the infos
    VCAP_SERVICES = os.getenv('VCAP_SERVICES')
    if VCAP_SERVICES is not None:
        app.config['dsn'] = get_elephantsql_dsn(VCAP_SERVICES)
    else:
        app.config['dsn'] = """user='vagrant' password='vagrant'
                               host='localhost' port=5432 dbname='itucsdb'"""
    app.run(host='0.0.0.0', port=port, debug=debug)
