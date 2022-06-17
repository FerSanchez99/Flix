from flask import Flask, request, render_template, redirect
from movies import models
import DBpsql as dbUser
import Login as l
import SignUp as su

app = Flask(__name__)
models.start_mappers()

@app.route("/", methods=["GET"])
def default():
    return redirect('/login')
    
@app.route("/login", methods=["GET"])
def login():
    return render_template('login.html')

@app.route("/signup", methods=["GET"])
def signup():
    return render_template('signup.html')

@app.route("/dashboard", methods=["GET"])
def dashboard():
    pk = dbUser.dbpsql().getPreferenceKey(dbUser.current_user)
    if pk == None: pk = -1
    return render_template('dashboard.html', preferenceKey = pk)

@app.route('/genres', methods=['GET'])
def genres():
    return render_template('genres.html')

@app.route('/auth_user', methods=['POST'])
def auth_user():
    email = request.form['email']
    password = request.form['password']
    if l.login().auth(email, password):
        return redirect('/dashboard')
    return redirect('/login')
    
@app.route('/create_user', methods=['POST'])
def create_user():
    email = request.form['email']
    password = request.form['password']
    su.signUp().registerUser(email, password)
    return redirect('/login')

@app.route('/save_pref', methods=['POST'])
def save_pref():
    c1 = request.form['cat1']
    c2 = request.form['cat2']
    c3 = request.form['cat3']
    pk = c1 + c2 + c3
    dbUser.dbpsql().savePreferences(dbUser.current_user, pk)
    return redirect('/dashboard')