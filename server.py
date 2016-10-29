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

app = Flask(__name__)


@app.route('/')
def home_page():
    now = datetime.datetime.now()
    return render_template('home.html', current_time=now.ctime())

@app.route('/dontrunthis')
def initialize():
    connection = dbapi2.connect(app.config['dsn'])
    try:
        cursor =connection.cursor()
        try:
            drop_tables(cursor)
            create_usertype_table(cursor)
            create_user_table(cursor)
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

@app.route('/users')
def users_page():
    return render_template('users.html')

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
