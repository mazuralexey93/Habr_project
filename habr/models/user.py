from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import check_password_hash

from habr.models.database import db
from habr.models.post import PostLike


class User(db.Model, UserMixin):
    __tablename__ = "users"

    liked = db.relationship('PostLike', foreign_keys='PostLike.user_id', backref='users', lazy='dynamic')

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    is_staff = db.Column(db.Boolean, nullable=False, default=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User {self.username}>"

    def like_post(self, post):
        if not self.has_liked_post(post):
            like = PostLike(user_id=self.id, post_id=post.id)
            db.session.add(like)

    def unlike_post(self, post):
        if self.has_liked_post(post):
            PostLike.query.filter_by(
                user_id=self.id,
                post_id=post.id).delete()

    def has_liked_post(self, post):
        return PostLike.query.filter(
            PostLike.user_id == self.id,
            PostLike.post_id == post.id).count() > 0


class Profile(db.Model):
    __tablename__ = "profile"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('users.id'))

    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    description = db.Column(db.Text())
    age = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    userpic = db.Column(db.LargeBinary)

    user = db.relationship('User', backref='profile', uselist=False)

    def __repr__(self):
        return f"<Profile {self.firstname} {self.lastname}>"
