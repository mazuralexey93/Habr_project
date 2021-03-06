from flask import Flask
from flask_ckeditor import CKEditor

import commands
from habr.instruments import login_manager

from config import Config
from habr.blueprints.posts import posts
from habr.blueprints.profile import profile
from habr.blueprints.auth import auth
from habr.blueprints.errors import errors

from habr.models.database import db, migrate
from habr.models.user import User


def create_app() -> Flask:
    app = Flask(__name__)
    ckeditor = CKEditor(app)
    app.config.from_object(Config)

    register_instruments(app)
    register_blueprints(app)
    register_commands(app)
    return app


def register_instruments(app):
    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = 'auth.login'  # путь к blueprint login
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app):
    app.register_blueprint(posts)
    app.register_blueprint(profile)
    app.register_blueprint(auth)
    app.register_blueprint(errors)


def register_commands(app):
    app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_init_user)
    app.cli.add_command(commands.create_init_post)
    app.cli.add_command(commands.create_init_profile)
