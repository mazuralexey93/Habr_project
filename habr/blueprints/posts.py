from flask import Blueprint, render_template
from habr.models.post import Post

posts = Blueprint(
    name='posts',
    import_name=__name__,
    template_folder='/templates',
    static_folder='/static')

#
# POSTS = db.session.query(
#     Post.category,
#     Post.user_id,
#     Post.created_at,
#     Post.body,
#     Post.header,
#     Post.description
# ).all()


@posts.route('/')
def post_list():
    postlist = Post.query.all()
    return render_template('index.html', postlist=postlist)


