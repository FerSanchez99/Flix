from flask import Flask, request, render_template, redirect
from movies import models
import controller as db

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
    return "Dashboard de Flix"

@app.route('/auth_user', methods=['POST'])
def auth_user():
    email = request.form['email']
    password = request.form['password']
    if db.read(email, password):
        return redirect('/dashboard') 
    return redirect('/login')
    
@app.route('/create_user', methods=['POST'])
def create_user():
    email = request.form['email']
    password = request.form['password']
    db.create(email, password)
    return redirect('/login')
    
    