from datetime import datetime
from flask_login import UserMixin

from habr.models.database import db


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    is_staff = db.Column(db.Boolean, nullable=False, default=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"<User {self.username}>"
