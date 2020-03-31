from sys import path
from . import User
from . import Challenge
from ctf import db
path.append("..")

# Work to do
# relationship with User (one user to many solve entries) and Challenge (one challenge to also many solve entries) tables


class Solve(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, db.ForeignKey('user.username'))
    challenge = db.Column(db.String, db.ForeignKey('challenge.name'))
    solved = db.Column(db.Boolean, default=False)
