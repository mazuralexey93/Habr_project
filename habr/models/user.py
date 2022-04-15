from datetime import datetime
from flask_login import UserMixin
from habr.models.database import db


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    is_staff = db.Column(db.Boolean, nullable=False, default=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"<User {self.username}>"


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
