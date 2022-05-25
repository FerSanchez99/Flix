from flask import Flask, request, render_template, redirect
from movies import models
from Login import Login
app = Flask(__name__)
models.start_mappers()


@app.route("/login", methods=["GET"])
def login():
    return render_template('login.html')


@app.route("/signup", methods=["GET"])
def signup():
    return "Creación de Cuenta"

@app.route("/dashboard", methods=["GET"])
def dashboard():
    return "Dashboard de Flix"


@app.route('/auth_user', methods=['POST'])
def auth_user():
    email = request.form['email']
    password = request.form['password']
    if Login.auth(email, password):
        return redirect("/dashboard")
    else:
        return "Contraseña inválida"
    