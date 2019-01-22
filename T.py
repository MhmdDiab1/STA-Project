from flask import Flask,render_template, flash, redirect, url_for, session, logging
from data import Trainees
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.handlers.sha2_crypt import sha512_crypt


app = Flask(__name__)

Trainees=Trainees()

@app.route('/')
def index():
    return render_template('login.html')

#@app.route('/',method=["GET","POST"])
#def login():
#    error=' '
#        if request.method=="POST":
#            attempted_username=request.form['username']
#            attempted_password=request.form['password']
#
#        if attempted_username=="admin" and attempted_password=="Password":
#            return redirect(url_for('/'))
#        else:
#            error="Wrong Username or Password. Try Again. "
#
#        return render_template("login.html")


@app.route('/Home')
def Home():
    return render_template('Home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/TraineeList')
def TraineeList():
    return render_template('TraineeList.html', trainees=Trainees)

@app.route('/add_Trainee')
def Add():
    return render_template('add_Trainee.html')

if __name__=='__main__':
   app.run(debug=True)