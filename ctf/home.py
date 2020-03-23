from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models.Score import Score
from . import db

home = Blueprint('home', __name__)


@home.route("/")
def index():
    return render_template("home.html")


@home.route("/profile")
@login_required
def profile():
    user_score = Score.query.filter_by(username=current_user.username).first()
    return render_template("profile.html", name=current_user.username, score=user_score.score)
