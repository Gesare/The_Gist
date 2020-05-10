from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import Email, Length, Required, EqualTo
from wtforms import ValidationError, PasswordField
from wtforms import StringField, SubmitField, TextAreaField

from app.models import User, Subscription


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=2, max=20)])

    email = StringField('Your Email Address', validators=[Email()])

    picture = FileField('Change Profile Picture', validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Update information')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    content = TextAreaField('Content', validators=[Required()])
    submit = SubmitField('Post')


class SubscribeForm(FlaskForm):
    email = StringField('Email address', validators=[Required(), Email()])
    submit = SubmitField('Subscribe')

    def validate_email(self, email):
        email = Subscription.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('That email is already subscribed to our emailing list.')


class CommentForm(FlaskForm):
    comment = StringField('Comment: ', validators=[Required()])
    submit = SubmitField('Submit')
