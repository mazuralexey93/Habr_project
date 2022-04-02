from flask import Flask, render_template

from habr.models.database import db
from posts.posts import posts


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "False"

    app.register_blueprint(posts, url_prefix='/posts')

    @app.route("/")
    def index():
        return render_template("index.html")

    db.init_app(app)
    return app
