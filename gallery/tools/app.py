from flask import Flask, redirect
from flask import request
from flask import render_template
from user_admin import UserAdmin

app = Flask(__name__)
user_admin = UserAdmin()


@app.route('/admin')
def list():
    #user_admin = UserAdmin()
    users = user_admin.list_accounts();
    return render_template('list.html', len=len(users), users=users)


@app.route('/admin/add')
def add():
    return render_template('add.html')


@app.route('/admin/addUser', methods=['POST'])
def add_new_user():
    #user_admin = UserAdmin()
    user_name = request.form['user_name']
    password = request.form['password']
    full_name = request.form['full_name']
    user_admin.add_account(user_name, password, full_name)
    return redirect('/admin')


@app.route('/admin/delete')
def delete():
    username = request.args['username']
    return render_template('delete.html', username=username)


@app.route('/admin/deleteUser')
def delete_user():
    #user_admin = UserAdmin()
    user_name = request.args['username']
    user_admin.del_account(user_name)
    return redirect('/admin')

@app.route('/admin/update')
def update():
    user_name = request.args['user_name']
    password = request.args['password']
    full_name = request.args['full_name']
    return render_template('update.html', username=user_name, password=password, full_name=full_name)

@app.route('/admin/updateUser', methods=['POST'])
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


