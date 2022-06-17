from flask import Flask, request, render_template, redirect, url_for
from movies import models
import DBpsql as dbUser
import Login as l
import SignUp as su



app = Flask(__name__)
models.start_mappers()

@app.route("/login", methods=["GET"])
def login():
    return render_template('login.html')

@app.route("/signup", methods=["GET"])
def signup():
    return render_template('signup.html')

@app.route("/dashboard", methods=["GET"])
def dashboard():

    return render_template('dashboard.html', user = dbUser.dbpsql.current_user)


@app.route('/genres', methods=['GET'])
def genres():
    return render_template('genres.html')

@app.route('/auth_user', methods=['POST'])
def auth_user():
    email = request.form['email']
    password = request.form['password']
    if l.login().auth(email, password):
        return redirect(url_for('dashboard', user_email=email))
    return redirect('/login')
    
@app.route('/create_user', methods=['POST'])
def create_user():
    email = request.form['email']
    password = request.form['password']
    su.signUp().registerUser(email, password)
    return redirect('/login')


    
    