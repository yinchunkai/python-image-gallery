from flask import Flask
from flask import request
from flask import render_template
# from user_admin import UserAdmin
from secrets import *

app = Flask(__name__)

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

@app.route('/goodbye')
def goodbye():
    return 'Goodbye'

@app.route('/greet/<name>')
def greet(name):
    return 'Nice to meet you ' + name

@app.route('/add/<int:x>/<int:y>', methods = ['GET'])
def add(x, y):
    return 'The sum is ' + str(x + y)

@app.route('/mult', methods=['POST'])
def mult():
    x = request.form['x']
    y = request.form['y']
    return 'The product is ' + str(x*y)

@app.route('/calculator/<personsName>')
def calculator(personsName):
    return render_template('calculator.html', name=personsName)
    
