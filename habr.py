from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app = Flask(__name__)

menu = ["Статьи", "Темы", "Обратная связь"]

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<users {self.id}>"

@app.route("/")
def index():
    return render_template('index.html', menu=menu)

@app.route("/about")
def about():
    return render_template('about.html', title="О сайте", menu=menu)

if __name__ == "__main__":
    app.run(debug=True)