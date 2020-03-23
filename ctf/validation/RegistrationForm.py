from wtforms import Form, StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email
from flask_wtf import FlaskForm


class RegistrationForm(FlaskForm):
    email = StringField(
        'Email', [DataRequired(), Email(), Length(min=6, max=36)])
    username = StringField(
        'Username', [DataRequired(), Length(min=3, max=36)])
    password = PasswordField(
        'Password', [DataRequired(), Length(min=8, max=36)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign Up')
