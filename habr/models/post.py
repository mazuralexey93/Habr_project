from datetime import datetime
import enum
from habr.models.database import db, CategoryChoices


class PostStatus(enum.Enum):
    NOT_PUBLISHED = 'черновик'
    PUBLISHED = 'опубликована'
    MODERING = 'на модерации'
    NEED_REFACTOR = 'требуется редактирование'
    ARCHIEVED = 'удалена'

    def __str__(self):
        return self.value


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
    status = db.Column(db.Enum(PostStatus, default=PostStatus.NOT_PUBLISHED))

    user = db.relationship('User', backref='post', uselist=False)


def __repr__(self):
    return f"<Post {self.id}, {self.header}>"
