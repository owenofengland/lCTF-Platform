from ctf import db
from ctf.models.Challenge import Challenge
from ctf.models.Score import Score
from ctf.models.User import User
from ctf.models.Solve import Solve
from ctf.validation.LoginForm import LoginForm
from ctf.validation.RegistrationForm import RegistrationForm
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from sys import path
path.append("..")

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=['POST', "GET"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        remember = form.remember_me.data

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash("Please check your login details and try again.")
            return redirect(url_for("auth.login"))
        else:
            login_user(user, remember=remember)
            return redirect(url_for("home.profile", username=user.username))
    elif request.method == "POST" and not form.validate_on_submit():
        errors = ["Email: " + error for error in form.email.errors]
        passwordErrors = ["Password: " +
                          error for error in form.password.errors]
        errors.extend(passwordErrors)
        flash(errors)
    return render_template("login.html", form=form)


@auth.route("/signup", methods=["POST", "GET"])
def signup():
    form = RegistrationForm()
    if request.method == "POST" and form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user:
            flash("Account with input email or username already exists")
            return redirect(url_for('auth.signup'))
        else:
            new_user = User(email=email,
                            password=generate_password_hash(password, method='sha256'), username=username)
            new_user_score = Score(score=0, username=new_user.username)

            challenges = Challenge.query.all()
            for challenge in challenges:
                this_Solve = Solve(username=username, challenge=challenge.name)
                db.session.add(this_Solve)

            db.session.add(new_user)
            db.session.add(new_user_score)
            db.session.commit()
            return redirect(url_for("auth.login"))
    elif request.method == "POST" and not form.validate_on_submit():
        errors = ["Email: " + error for error in form.email.errors]
        passwordErrors = ["Password: " +
                          error for error in form.password.errors]
        usernameErrors = ["Username: " +
                          error for error in form.username.errors]
        errors.extend(passwordErrors)
        errors.extend(usernameErrors)
        flash(errors)
    return render_template("signup.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home.index"))
