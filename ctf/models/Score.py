from . import User
from ctf import db
from sys import path
path.append("..")


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, default=0)
    username = db.Column(db.String, db.ForeignKey('user.username'))
