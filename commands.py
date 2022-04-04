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
            User(username='admin', email='admin@mail.com', is_staff=True, is_admin=True),
            User(username='moder', email='moder@mail.com', is_staff=True, is_admin=False),
            User(username='user', email='user@mail.com'),
            User(username='inactive_user', email='inactive_user@mail.com', is_active=False)])

        db.session.commit()


@click.command('create-init-post')
def create_init_post():
    from habr.models.post import Post, CategoryChoices
    from wsgi import app

    with app.app_context():
        db.session.add_all([
            Post(category=CategoryChoices.MOBILE, header='Smthg new!', body='Content', description='short_description', user_id=1),
            Post(category=CategoryChoices.MARKETING, header='Smthg new!', body='Content', description='short_description', user_id=2),
            Post(category=CategoryChoices.WEB, header='Smthg new!', body='Content', description='short_description', user_id=3),
            Post(category=CategoryChoices.DESIGN, header='Smthg new!', body='Content', description='short_description', user_id=4),
            Post(category=CategoryChoices.WEB, header='Smthg new!', body='Content', description='short_description', user_id=1)])
        db.session.commit()
