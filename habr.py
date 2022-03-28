from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request

app = Flask(__name__)

menu = ["Статьи", "Темы", "Обратная связь"]

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(80), unique=True, nullable=False)
    # email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    passwd = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"<users {self.id}>"

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<posts {self.id}>"

db.create_all()

@app.route("/")
def index():
    return render_template('index.html', menu=menu)

@app.route("/about")
def about():
    return render_template('about.html', title="О сайте", menu=menu)

@app.route("/register", methods=("POST", "GET"))
def register():
    if request.method == "POST":
        try:
            hash = generate_password_hash(request.form['passwd'])
            u = Users(email=request.form['email'], passwd=hash)
            db.session.add(u)
            db.session.commit()
            print("Пользователь добавлен")
        except:
            db.session.rollback()
            print("Ошибка добавления в БД")

    return render_template('register.html', title="Регистрация", menu=menu)

if __name__ == "__main__":
    app.run(debug=True)