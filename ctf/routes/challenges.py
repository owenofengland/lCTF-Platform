from ctf import db
from ctf.models.Challenge import Challenge
from ctf.models.Category import Category
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from sys import path
path.append("..")

challenges = Blueprint("challenges", __name__)


@challenges.route("/challenges", methods=["GET"])
def challenges_list():
    pass
