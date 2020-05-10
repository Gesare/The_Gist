from datetime import datetime

from flask import url_for, app, config
from werkzeug.utils import redirect

from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, index=True, nullable=False)
    image_file = db.Column(db.String(70), nullable=False, default='default.jpg')
    comments = db.relationship('Comments', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'User {self.username}'

    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(15), nullable=False, default='Keith Mzaza')
    comment = db.relationship('Comments', backref='post', lazy='dynamic')

    def __repr__(self):
        return f"Post( '{self.title}', '{self.date_posted}')"


class Subscription(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, index=True, nullable=False)

    def __repr__(self):
        return f'{self.email}'


class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(10000))
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_comments(self):
        db.session.add(self)
        db.session.commit()
