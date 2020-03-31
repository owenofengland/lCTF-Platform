from . import Challenge
from sys import path
from ctf import db
path.append("..")


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    challenges = db.relationship("Challenge", backref="category_challenge")
