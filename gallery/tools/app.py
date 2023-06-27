from flask import Flask, redirect
from flask import request
from flask import render_template
from user_admin import UserAdmin
from flask import session

from user import User
from postgres_user_dao import PostgresUserDAO
from db import Db

from functools import wraps

app = Flask(__name__)
app.secret_key = b'fowerwksdfoef'
user_admin = UserAdmin()
Db.connect()

def get_user_dao():
    return PostgresUserDAO

def check_admin():
    return 'username' in session and session['username'] == 'fred'


def requires_admin(view):
    @wraps(view)
    def decorated(**kwargs):
        if not check_admin():
            return redirect('/login')
        return view(**kwargs)
    return decorated


@app.route('/invalidLogin')
def invalidLogin():
    return "Invalid"


@app.route('/upload')
def invalidLogin():
    return "In process..."


@app.route('/view')
def invalidLogin():
    return "In process..."


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = get_user_dao().get_user_by_username(request.form["username"])
        if user is None or user.password != request.form["password"]:
            return redirect('/invalidLogin')
        else:
            session['username'] = request.form["username"]
            return redirect("/debugSession")
    else:
        return render_template("login.html")


@app.route('/debugSession')
def debugSession():
    result = ""
    for key, value in session.items():
        result +=key + "->" + str(value) + "<br />"
    return result


@app.route('/admin/users')
@requires_admin
def list():
    #user_admin = UserAdmin()
    users = user_admin.list_accounts();
    return render_template('list.html', len=len(users), users=users)


@app.route('/admin/add')
@requires_admin
def add():
    return render_template('add.html')


@app.route('/admin/addUser', methods=['POST'])
@requires_admin
def add_new_user():
    #user_admin = UserAdmin()
    user_name = request.form['user_name']
    password = request.form['password']
    full_name = request.form['full_name']
    user_admin.add_account(user_name, password, full_name)
    return redirect('/admin')


@app.route('/admin/delete')
@requires_admin
def delete():
    username = request.args['username']
    return render_template('delete.html', username=username)


@app.route('/admin/deleteUser')
@requires_admin
def delete_user():
    #user_admin = UserAdmin()
    user_name = request.args['username']
    user_admin.del_account(user_name)
    return redirect('/admin')

@app.route('/admin/update')
@requires_admin
def update():
    user_name = request.args['user_name']
    password = request.args['password']
    full_name = request.args['full_name']
    return render_template('update.html', username=user_name, password=password, full_name=full_name)

@app.route('/admin/updateUser', methods=['POST'])
@requires_admin
def update_user():
    #user_admin = UserAdmin()
    user_name = request.form['user_name']
    password = request.form['password']
    full_name = request.form['full_name']
    print("new data:" + user_name +","+password+","+full_name)
    user_admin.edit_account(user_name, password, full_name)
    return redirect('/admin')


@app.route('/')
def hello_world():
    return """
<!DOCTYPE html>
<html>
   <head>
      <title>Hello</title>
      <meta charset="utf-8" />
   </head>
   <body>
     <h1>Hello, David!</h1>
   </body>
</html>
"""


