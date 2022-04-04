from flask import Flask, render_template

from habr.models.database import db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "False"

    @app.route("/")
    def index():
        return render_template("index.html")

    db.init_app(app)
    register_blueprints(app)
    return app

def register_blueprints(app):
    from .blueprints.post_list import posts
    from .blueprints.user import users

    app.register_blueprint(posts, url_prefix='/posts')
    app.register_blueprint(users, url_prefix='/users')
