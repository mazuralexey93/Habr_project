from flask import Flask, render_template

import commands
from config import Config
from habr.models.database import db, migrate


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route("/")
    def index():
        return render_template("index.html")

    db.init_app(app)
    migrate.init_app(app, db)
    register_commands(app)
    return app


def register_commands(app):
    app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_init_user)
    app.cli.add_command(commands.create_init_post)


