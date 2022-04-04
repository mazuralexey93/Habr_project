
from datetime import datetime

from habr.models.database import db, CategoryChoices


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.Enum(CategoryChoices))
    # category = db.Column(
    #     db.Enum(CategoryChoices,
    #             values_callable=lambda x: [str(cat.value)
    #                                        for cat in CategoryChoices]))
    header = db.Column(db.String(255))
    body = db.Column(db.Text())
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(), index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), index=True, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # image = db.Column(db.String(64))

    def __repr__(self):
        return f"<Post {self.id}, {self.header}>"
