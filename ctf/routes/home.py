from flask import Blueprint, render_template
from flask_login import login_required, current_user
from ctf.models.Score import Score
from ctf.models.User import User
from ctf import db
from sys import path
path.append("..")

home = Blueprint('home', __name__)


@home.route("/", methods=["GET"])
def index():
    return render_template("home.html")


@home.route("/profile", methods=["GET"])
@login_required
def profile():
    user_score = Score.query.filter_by(username=current_user.username).first()
    return render_template("profile.html", name=current_user.username, score=user_score.score)


@home.route("/profile/<username>", methods=["GET"])
@login_required
def view_profile(username):
    user = User.query.filter_by(username=username).first()
    score = Score.query.filter_by(username=user.username).first()
    return render_template('profile.html', name=user.username, score=score.score)


@home.route("/about", methods=["GET"])
def about():
    return render_template("about.html")
