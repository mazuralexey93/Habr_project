from flask import Flask

import commands
from config import Config
from habr.models.database import db, migrate, login_manager, csrf
from .models.user import User


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    csrf.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    register_blueprints(app)
    register_commands(app)
    return app


def register_blueprints(app):
    from habr.blueprints.posts import posts
    from habr.blueprints.auth import auth
    app.register_blueprint(posts)
    app.register_blueprint(auth)


def register_commands(app):
    app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_init_user)
    app.cli.add_command(commands.create_init_post)


