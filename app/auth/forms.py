from flask_wtf import FlaskForm
from wtforms.validators import Required, Email, EqualTo, Length
from wtforms import ValidationError
from wtforms import StringField, PasswordField, BooleanField, SubmitField

from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[Required(), Length(min=2, max=20)])
    email = StringField('Your Email Address', validators=[Required(), Email()])
    password = PasswordField('Password', validators={Required(),
                                                     EqualTo('password_confirm', message='Passwords must match')})
    password_confirm = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('That username is taken')


class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
