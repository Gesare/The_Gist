from flask_wtf import FlaskForm
from wtforms.validators import Required, Email, EqualTo, Length
from wtforms import ValidationError
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from app.models import User


class RegistrationForm(FlaskForm):
    email = StringField('Enter Email Address', validators=[Required(), Email()])
    username = StringField('Username', validators=[Required(), Length(min=2, max=20)])
    password = PasswordField('Password', validators={Required(),                                                EqualTo('password_confirm', message='Passwords must match')})
    password_confirm = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Enter Email Address', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')


