import click
from habr.models.database import db



@click.command('init-db')
def init_db():
    from wsgi import app

    db.create_all(app=app)


@click.command('create-init-user')
def create_init_user():
    from habr.models.user import User
    from wsgi import app

    with app.app_context():
        db.session.add_all([
            User(username='admin', email='admin@mail.com', password='12345qqq', is_staff=True, is_admin=True),
            User(username='moder', email='moder@mail.com', password='12345qqq', is_staff=True, is_admin=False),
            User(username='user', email='user@mail.com', password='12345qqq'),
            User(username='empty_user', email='empty_user@mail.com', password='12345qqq'),
            User(username='inactive_user', email='inactive_user@mail.com', password='12345qqq', is_active=False)])

        db.session.commit()


@click.command('create-init-post')
def create_init_post():
    from habr.models.post import Post, CategoryChoices, PostStatus
    from wsgi import app

    with app.app_context():
        db.session.add_all([
            Post(category=CategoryChoices.MOBILE, status=PostStatus.NOT_PUBLISHED, header='Smthg new!', body='Content', description='short_description', user_id=1),
            Post(category=CategoryChoices.MARKETING, status=PostStatus.PUBLISHED, header='Smthg new!', body='Content', description='short_description', user_id=2),
            Post(category=CategoryChoices.WEB, status=PostStatus.MODERING,header='Smthg new!', body='Content', description='short_description', user_id=3),
            Post(category=CategoryChoices.DESIGN, status=PostStatus.NEED_REFACTOR, header='Smthg new!', body='Content', description='short_description', user_id=4),
            Post(category=CategoryChoices.WEB, status=PostStatus.ARCHIEVED,header='Smthg new!', body='Content', description='short_description', user_id=1)])
        db.session.commit()


@click.command('create-init-profile')
def create_init_profile():
    from habr.models.user import Profile
    from wsgi import app

    with app.app_context():
        db.session.add_all([
            Profile(firstname='vasya', lastname='ivanov', age=30, description='just user 1', user_id=1),
            Profile(firstname='sanya', lastname='gomer', age=32,  description='just user 2', user_id=2),
            Profile(firstname='nika', lastname='buzova', age=15,  description='just user 3', user_id=3),
            Profile(firstname='oler', lastname='kislyj', age=23,  description='just user 4', user_id=4),
            Profile(firstname='maria', lastname='petrova', age=40, description='just user 5', user_id=5)])
        db.session.commit()
