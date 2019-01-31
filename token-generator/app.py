from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, redirect, url_for, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_sqlalchemy  import SQLAlchemy
from functools import wraps
from uuid import uuid4
import subprocess
import smtplib
import uuid
import jwt
from uuid import uuid4
import datetime

app = Flask(__name__)
db = SQLAlchemy(app)
login_manager = LoginManager()

# Set up Main config
app.config['SECRET_KEY'] = 'qZjvXHxDv7Dcsv2a0IrmGZ5KNKZ10gO'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DataBase/example.db'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LcpbWAUAAAAAAHfKwXV_vDW3f5gP1ET0PHsvEOp'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LcpbWAUAAAAABQidUSjPpv2K1AevKrTfSB9CYiN'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(60), unique=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(80))
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    email = db.Column(db.String(30))
    status = db.Column(db.String(10))
    role = db.Column(db.String(10))
    group = db.Column(db.String(20))

class token_manager(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(60), unique=True)



@app.route('/')
def index():
    return jsonify({'User': data})

@app.route('/gen', methods=['POST', 'GET'])
def generator():
    return jsonify({'missing': 'token'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
