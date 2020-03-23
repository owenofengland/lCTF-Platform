from flask_login import UserMixin
from ctf import db
from sys import path
from . import Score
path.append("..")


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    score = db.relationship('Score', backref="user", uselist=False)
