from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models.User import User
from .models.Score import Score
from . import db

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/login", methods=['POST'])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash("Please check your login details and try again.")
        return redirect(url_for("auth.login"))
    else:
        login_user(user, remember=remember)
        return redirect(url_for("home.profile"))


@auth.route("/signup")
def signup():
    return render_template("signup.html")


@auth.route("/signup", methods=["POST"])
def signup_post():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")

    print(username)

    user = User.query.filter_by(email=email).first()

    if user:
        flash("Account with input email or username already exists")
        return redirect(url_for('auth.signup'))
    else:
        new_user = User(email=email,
                        password=generate_password_hash(password, method='sha256'), username=username)
        new_user_score = Score(score=0, user=new_user)
        db.session.add(new_user)
        db.session.add(new_user_score)
        db.session.commit()
        return redirect(url_for("auth.login"))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home.index"))
