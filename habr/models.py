from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from habr import db


roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('roles.id'))
)


class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return f'<Role {self.name}>'


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password = db.Column(db.String(64))
    active = db.Column(db.Boolean(), default=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    def has_role(self, *args):
        return set(args).issubset({role.name for role in self.roles})

    def get_id(self):
        return self.id

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    def __repr__(self):
        return f'<User {self.username}>'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(64))
    header = db.Column(db.String(64))
    body = db.Column(db.String(140))
    short_description = db.Column(db.String(140))
    created_at = db.Column(db.DateTime(), index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), index=True, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # image = db.Column(db.String(64))

    def get_id(self):
        return self.id

    def get_user(self):
        return self.user_id

    def __repr__(self):
        return f'<Post {self.id}, {self.header}>'
