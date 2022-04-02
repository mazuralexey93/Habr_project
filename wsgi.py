from habr.app import create_app
from habr.models.post import Post, CategoryChoices
from habr.models.user import User

from habr.app import db

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Categories': CategoryChoices}
