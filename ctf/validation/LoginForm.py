from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    email = StringField(
        "Email", [DataRequired(), Email(), Length(min=6, max=36)])
    password = PasswordField(
        "Password", [DataRequired(), Length(min=8, max=36)])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Log In")
