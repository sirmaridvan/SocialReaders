import datetime
import os
import json
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
from flask.globals import session
from Groups import *

app = Flask(__name__)


@app.route('/')
def home_page():
    now = datetime.datetime.now()
    return render_template('home.html', current_time=now.ctime())
@app.route('/blogs')
def blogs_page():
    return render_template('blogs.html')

@app.route('/insertBlogPost', methods=['POST'])
def insert_blog_post():

    if request.method == 'POST':
        #your database process here
        userName = createRandomUserName()
        date=datetime.datetime.now()
        header="header"
        text="text"
        blogPost = BlogPost(0,userName,datetime.date.today(),header,text);

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
        return "OK"
    else:
        return "NO OK"

@app.route('/dontrunthis')
def initialize():
    connection = dbapi2.connect(app.config['dsn'])
    try:
        cursor =connection.cursor()
        try:
            drop_tables(cursor)
            create_usertype_table(cursor)
            create_user_table(cursor)
            create_blogs_table(cursor)
            insert_usertype(cursor,'Admin')
            insert_usertype(cursor,'User')

            salt1 = createRandomSalt()
            user1 = User(0,'benlielif','123456',salt1,createHash(salt1,'123456'),'elfbnli@gmail.com','Elif','Benli',1)
            salt2 = createRandomSalt()
            user2 = User(0,'uyar','123456',salt2,createHash(salt2,'123456'),'uyar@itu.edu.tr','Turgut','Uyar',1)
            insert_siteuser(cursor,user1)
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

    create_groups_table()
    create_members_table()
    insert_group(group1)
    insert_member(1,1)

    '''create_author_table()
    insert_author(author1)
    insert_author(author2)


    cursor =connection.cursor()
    create_book_table(cursor)
    create_genre_table(cursor)
    create_quote_table(cursor)


    insert_genre(genre1)
    insert_genre(genre2)
    insert_book(book1)
    insert_book(book2)
    insert_quote(quote1)
    insert_quote(quote2)'''


    return redirect(url_for('home_page'))

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
                    ((salt,hash),) =  cursor.fetchall()
                    if hash == createHash(salt,request.form['password']):
                        session['logged_in'] = True
                elif "register-submit" in request.form:
                    salt = createRandomSalt()
                    getUserType(cursor,'User')
                    ((typeid),) = cursor.fetchall()
                    insert_siteuser(cursor,User(0,request.form['username'], request.form['password'], salt, createHash(salt,request.form['password']),request.form['email'],request.form['name'],request.form['surname'],typeid))
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
            return redirect(url_for('home_page'))

    return render_template('login.html')

@app.route('/authors',methods=['GET', 'POST'])
def authors_page():
    return render_template('authors.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile_page():
    return render_template('profile.html')

@app.route('/news')
def news_page():
    return render_template('news.html')

@app.route('/bookpage')
def book_page():
    return render_template('bookpage.html')

@app.route('/users',methods=['GET', 'POST'])
def users_page():
    connection = dbapi2.connect(app.config['dsn'])
    try:
        cursor =connection.cursor()
        try:
            if request.method == 'POST':
                if "edit" in request.form:
                    userid = request.form['editid']

                elif "delete" in request.form:
                    userid = request.form['deleteid']
                    deleteUser(cursor,userid)
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

@app.route('/userupdate',methods=['GET', 'POST'])
def userUpdate_page():
    connection = dbapi2.connect(app.config['dsn'])
    try:
        cursor =connection.cursor()
        try:
            if request.method == 'GET':
                userid = request.args.get('id')
                getUserById(cursor,userid)
                ((id,username,salt,hash,email,name,surname,usertypeid),) = cursor.fetchall()
                mUser = User(id,username,"",salt,hash,email,name,surname,usertypeid)
                return render_template('userupdate.html',user = mUser)
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

def get_elephantsql_dsn(vcap_services):
    """Returns the data source name for ElephantSQL."""
    parsed = json.loads(vcap_services)
    uri = parsed["elephantsql"][0]["credentials"]["uri"]
    match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
    user, password, host, _, port, dbname = match.groups()
    dsn = """user='{}' password='{}' host='{}' port={}
             dbname='{}'""".format(user, password, host, port, dbname)
    return dsn

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
