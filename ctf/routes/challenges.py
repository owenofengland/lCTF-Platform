from ctf import db
from ctf.models.Challenge import Challenge
from ctf.models.Category import Category
from ctf.models.Score import Score
from ctf.models.Solve import Solve
from ctf.validation.ChallengeForm import ChallengeForm
from ctf.util.flag_generator import generate_flag_buffer
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from sys import path
path.append("..")

challenges = Blueprint("challenges", __name__)


@challenges.route("/challenges", methods=["GET"])
@login_required
def challenges_list():
    categories = Category.query.all()
    grid = []

    for category in categories:
        row = [category]
        challenges = Challenge.query.filter_by(category_id=category.name)
        for challenge in challenges:
            row.append(challenge)
        if len(row) > 1:
            grid.append(row)

    return render_template("challenges.html", grid=grid)


@challenges.route("/challenge/<id>", methods=["GET", "POST"])
@login_required
def challenge(id):
    form = ChallengeForm()
    this_challenge = Challenge.query.filter_by(id=id).first()
    current_user_score = Score.query.filter_by(
        username=current_user.username).first()
    current_user_solve = Solve.query.filter_by(
        username=current_user.username, challenge=this_challenge.name).first()

    if this_challenge:
        name = this_challenge.name
        value = this_challenge.value
        solves = this_challenge.solves
        desc = this_challenge.desc
        cur_flag = this_challenge.cur_flag
        category = this_challenge.category_id

        if request.method == "POST" and form.validate_on_submit():
            guess = form.guess.data
            if guess == cur_flag:
                if current_user_solve.solved:
                    flash("Already submitted correct flag!")
                else:
                    flash("Success! Correct flag submitted!")
                    current_user_score.score = current_user_score.score + value
                    current_user_solve.solved = True
                    this_challenge.cur_flag = generate_flag_buffer(this_challenge.base_flag)
                    db.session.commit()
            else:
                flash("Flag is invalid")

        return render_template("challenge.html", form=form, name=name, value=value, solves=solves, category=category)
    else:
        return "Error, challenge does not exist"
