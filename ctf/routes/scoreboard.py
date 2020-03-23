from flask import Blueprint, render_template
from flask_login import login_required, current_user
from ctf.models.Score import Score
from ctf import db
from sys import path
path.append("..")

scoreboard = Blueprint("scoreboard", __name__)


@scoreboard.route("/scoreboard")
def scoreboard_out():
    scores = Score.query.all()
    scores.sort(key=lambda x: x.score, reverse=True)
    return render_template("scoreboard.html", scores=scores)
