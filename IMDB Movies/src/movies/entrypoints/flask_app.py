from flask import Flask, request, render_template, redirect
from movies import models
import Login as l
import SignUp as su
import Recommendation as r
import movie_fetcher as mf

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
    user = r.recommendation().getUser()
    pk = r.recommendation().getPK(user)
    ordered = r.recommendation().getOrderedSetting(user)
    movies_rec = []
    if pk:
        movies_rec = r.recommendation().getMoviesRec(pk, ordered)
    if pk == None: pk = -1
    return render_template('dashboard.html', movies_rec = movies_rec, preferenceKey = pk)

@app.route('/genres', methods=['GET'])
def genres():
    return render_template('genres.html')

@app.route('/auth_user', methods=['POST'])
def auth_user():
    if r.recommendation().isMoviesTableEmpty():
        mf.main() #only called once to init movies table
    email = request.form['email']
    password = request.form['password']
    if l.login().auth(email, password):
        return redirect('/dashboard')
    return redirect('/login')
    
@app.route('/create_user', methods=['POST'])
def create_user():
    email = request.form['email']
    password = request.form['password']
    su.signUp().register(email, password)
    return redirect('/login')

@app.route('/save_pref', methods=['POST'])
def save_pref():
    user = r.recommendation().getUser()
    c1 = request.form['cat1']
    c2 = request.form['cat2']
    c3 = request.form['cat3']
    try:
        order = request.form['ordered']
    except:
        order = 'false'
    r.recommendation().setPreferences(user, c1, c2, c3, order)
    return redirect('/dashboard')