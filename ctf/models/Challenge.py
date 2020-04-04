from sys import path
from . import Category
from . import Solve
from ctf import db
path.append("..")


class Challenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    value = db.Column(db.Integer)
    requirement = db.Column(db.Integer)
    solves = db.Column(db.Integer, default=0)
    desc = db.Column(db.String(300))
    base_flag = db.Column(db.String(100))
    cur_flag = db.Column(db.String(100))
    category_id = db.Column(db.String, db.ForeignKey('category.name'))
    solve = db.relationship("Solve", backref="challenge_solve")
