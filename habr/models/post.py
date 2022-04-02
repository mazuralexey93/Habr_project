from datetime import datetime

from habr.models.database import db


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(64))
    header = db.Column(db.String(64))
    body = db.Column(db.String(140))
    short_description = db.Column(db.String(140))
    created_at = db.Column(db.DateTime(), index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), index=True, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # image = db.Column(db.String(64))

    def __repr__(self):
        return f"<Post {self.id}, {self.header}>"
