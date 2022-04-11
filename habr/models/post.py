from datetime import datetime

from habr.models.database import db, CategoryChoices


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('users.id'))

    category = db.Column(db.Enum(CategoryChoices))
    header = db.Column(db.String(255))
    body = db.Column(db.Text())
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(), index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), index=True, default=datetime.utcnow, onupdate=datetime.utcnow)
    image = db.Column(db.LargeBinary)

    user = db.relationship('User', backref='post', uselist=False)


def __repr__(self):
    return f"<Post {self.id}, {self.header}>"
