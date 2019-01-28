from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from wtforms.validators import (InputRequired, Regexp, ValidationError, Email,
                               Length, EqualTo, Optional)

from models import User

WSCENTERS = [
    ("Ohio-Kentucky-Indiana", "Ohio-Kentucky-Indiana Water Science Center"),
    ("Illinois", "Illinois Water Science Center"),
    ("California", "California Water Science Center"),
]

def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError("User with that email already exists.") 


class RegisterForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            InputRequired(),
            Email(message=("Please enter a valid email address.")),
            email_exists
        ])

    password = PasswordField(
        "Password",
        validators=[
            InputRequired(),
            Length(min=8, message=("Passwords must have a minimum of 8 characters."))
        ])

    wsc = SelectField(
        "Water Science Center",
        choices=WSCENTERS,
        validators=[
            InputRequired()
        ])


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])


class QAForm(FlaskForm):
    responsibilities = TextAreaField(
        "Responsibilities Specifics", 
        description="Add Specific Information", 
        validators=[Optional()])

    safety = TextAreaField(
        "Safety Specifics", 
        description="Add Specific Information",
        validators=[Optional()])

    stream_install = TextAreaField(
        "Stream Installation and Maintenance Specifics", 
        description="Add Specific Information",
        validators=[Optional()])

    station_desc = TextAreaField(
        "Station Description Specifics", 
        description="Add Specific Information",
        validators=[Optional()])

    station_photos = TextAreaField(
        "Station Photos and Videos Specifics", 
        description="Add Specific Information",
        validators=[Optional()])

