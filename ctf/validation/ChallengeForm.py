from wtforms import Form, StringField, SubmitField
from flask_wtf import FlaskForm


class ChallengeForm(FlaskForm):
    guess = StringField("Flag")
    submit = SubmitField("Submit")
