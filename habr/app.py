from flask import Flask

import commands
from config import Config
from habr.models.database import db, migrate


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    register_blueprints(app)
    register_commands(app)
    return app


def register_blueprints(app):
    from habr.blueprints.posts import posts
    app.register_blueprint(posts)


def register_commands(app):
    app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_init_user)
    app.cli.add_command(commands.create_init_post)


