from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError
from app.auth.models import Users
from app import bcrypt
import os


def check_email(form, field):
    email_exist = Users.query.filter_by(user_email=field.data).first()
    if email_exist:
        raise ValidationError(
            'email already exist, please go to login page')


# check user credential to login
def check_credentials(form, field):
    user_email = form.email.data
    # if email exist then check if password match
    user = Users.query.filter_by(user_email=user_email).first()
    if user is None:
        raise ValidationError('Invalid credentials, please enter email and password correctly')
    elif bcrypt.check_password_hash(user.user_password, field.data) == False:
        raise ValidationError('Invalid credentials, please enter email and password correctly')


class RegForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email(message="please enter a valid email format"), check_email])
    password = PasswordField("password", validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password',message='Passwords must match')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(
        message="please enter a valid email format")])
    password = PasswordField("password", validators=[DataRequired(), check_credentials])
    submit = SubmitField('Login')
    remember_me = BooleanField("Remember me")


class DeleteForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(
        message="please enter a valid email format")])
    password = PasswordField("password", validators=[DataRequired(), check_credentials])
    submit = SubmitField('Delete')


class SearchForm(FlaskForm):
    what = StringField("what")
    where = StringField("Where", validators=[DataRequired()])

