from ctf import db
from ctf.models.Challenge import Challenge
from ctf.models.Category import Category
from ctf.models.Score import Score
from ctf.validation.ChallengeForm import ChallengeForm
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from sys import path
path.append("..")

challenges = Blueprint("challenges", __name__)


@challenges.route("/challenges", methods=["GET"])
@login_required
def challenges_list():
    categories = Category.query.all()
    return categories


@challenges.route("/challenge/<id>", methods=["GET", "POST"])
@login_required
def challenge(id):
    form = ChallengeForm()
    this_challenge = Challenge.query.filter_by(id=id).first()
    current_user_score = Score.query.filter_by(
        username=current_user.username).first()

    if this_challenge:
        name = this_challenge.name
        value = this_challenge.value
        solves = this_challenge.solves
        desc = this_challenge.desc
        flag = this_challenge.flag
        category = this_challenge.category_id

        if request.method == "POST" and form.validate_on_submit():
            guess = form.guess.data
            if guess == flag:
                flash("Success! Correct flag submitted!")
                current_user_score.score = current_user_score.score + value
                db.session.commit()
            else:
                flash("Flag is invalid")

        return render_template("challenge.html", form=form, name=name, value=value, solves=solves, category=category)
    else:
        return "Error, challenge does not exist"
