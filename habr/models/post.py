import enum
from datetime import datetime

from habr.models.database import db


class CategoryChoices(enum.Enum):
    DESIGN = 'Design'
    WEB = 'Web'
    MOBILE = 'Mobile'
    MARKETING = 'Marketing'

    @staticmethod
    def fetch_categories():
        return [c.value for c in CategoryChoices]


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.Enum(CategoryChoices))
    header = db.Column(db.String(255))
    body = db.Column(db.Text())
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(), index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), index=True, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # image = db.Column(db.String(64))

    def __repr__(self):
        return f"<Post {self.id}, {self.header}>"
