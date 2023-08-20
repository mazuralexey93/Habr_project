from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from werkzeug.exceptions import NotFound, Forbidden

from habr.models.post import Post, CategoryChoices, PostStatus, Comment
from habr.models.user import User
from habr.models.database import db
from habr.forms.post import AddCommentForm, CreateArticleForm, UpdateCommentForm

themes_dic = {
    'design': 'Дизайн',
    'web': 'Веб-разработка',
    'mobile': 'Мобильная разработка',
    'marketing': 'Маркетинг',
}

posts = Blueprint(
    name='posts',
    import_name=__name__,
    template_folder='/templates',
    static_folder='/static')


@posts.route('/')
def post_list():
    status = 'published'
    postlist = Post.query.filter(Post.status == status.upper()).order_by(Post.created_at.desc()).all()
    return render_template('index.html', menu='main', title="Главная страница",
                           pageheader="Главная страница", postlist=postlist)


@posts.route("/theme/<theme_name>/")
def theme_filter(theme_name: str):
    status = 'published'
    if theme_name not in themes_dic.keys():
        raise NotFound('Нет такой категории!')
    postlist = Post.query.filter(Post.status == status.upper()).filter(Post.category == theme_name.upper()).order_by(
        Post.created_at.desc()).all()
    return render_template('index.html', menu=theme_name,
                           pageheader=themes_dic[theme_name],
                           title=themes_dic[theme_name], postlist=postlist)


@posts.route("/author/<int:pk>/")
def author_filter(pk: int):
    status = 'published'
    author = User.query.filter_by(id=pk).first_or_404()
    postlist = Post.query.filter(Post.status == status.upper()).filter_by(user_id=pk).order_by(
        Post.created_at.desc()).all()
    title = f'Все статьи автора {author.username}'
    return render_template('index.html', title=title, postlist=postlist)


@login_required
@posts.route('/post/<int:pk>', methods=['GET', 'POST'])
def concrete_post(pk: int):
    selected_post = Post.query.filter_by(id=pk).first_or_404()
    # if selected_post.user != current_user:
    #     raise Forbidden()
    comment = Comment.query.filter_by(post_id=pk).order_by(db.desc(Comment.date_posted)).all()
    selected_post.views += 1
    db.session.commit()
    form = AddCommentForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = current_user.username
            comment = Comment(username=username, body=form.body.data, post_id=pk)
            db.session.add(comment)
            db.session.commit()
            return redirect(url_for('posts.concrete_post', pk=pk))
    title = selected_post.user.username + ' «' + selected_post.header + '»'
    return render_template('article.html', post=selected_post, title=title, comment=comment, form=form, post_id=pk)


@login_required
@posts.route('/post/create/', methods=['GET', 'POST'])
def create_article():
    form = CreateArticleForm(request.form)
    form.category.choices = [x for x in CategoryChoices.__members__]
    form.status.choices = [y for y in PostStatus.__members__ if
                           y != 'PUBLISHED' and y != 'NEED_REFACTOR' and y != 'ARCHIEVED']

    if request.method == "POST" and form.validate_on_submit():
        post = Post(category=form.category.data, header=form.title.data, body=form.text.data,
                    description=form.description.data, status=form.status.data)
        if current_user:
            post.user_id = current_user.id
        else:
            user = User(user_id=current_user.id)
            db.session.add(user)
            db.session.flush()
            post.status = PostStatus.NOT_PUBLISHED
            post.user_id = user.id
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('posts.post_list'))

    return render_template('article_create.html', form=form)


@login_required
@posts.route('/post/update/<int:pk>/', methods=['GET', 'POST'])
def update_article(pk):
    form = CreateArticleForm(request.form)
    form.category.choices = [x for x in CategoryChoices.__members__]
    form.status.choices = [y for y in PostStatus.__members__ if y != 'PUBLISHED' and y != 'NEED_REFACTOR']
    post = Post.query.get_or_404(pk)

    if request.method == "POST" and form.validate_on_submit():
        post.header = form.title.data
        post.category = form.category.data
        post.description = form.description.data
        post.status = form.status.data
        post.body = form.text.data
        db.session.add(post)
        db.session.commit()
        flash('Post has been updated!')
        return redirect(url_for('posts.concrete_post', pk=pk))

    form.title.data = post.header
    form.description.data = post.description
    form.text.data = post.body
    return render_template('article_update.html', form=form)


@posts.route('/post/delete/<int:pk>')
def delete_article(pk: int):
    post = Post.query.get_or_404(pk)

    if post.user == current_user or current_user.is_admin:
        post.status = PostStatus.ARCHIEVED
        db.session.add(post)
        db.session.commit()
    return redirect(url_for('posts.concrete_post', pk=pk))


@posts.route('/post/need_ref/<int:pk>')
def need_ref_article(pk: int):
    post = Post.query.get_or_404(pk)
    if current_user.is_staff or current_user.is_admin:
        post.status = PostStatus.NEED_REFACTOR
        db.session.add(post)
        db.session.commit()
    return redirect(url_for('posts.concrete_post', pk=pk))


@posts.route('/post/publish/<int:pk>')
def pub_article(pk: int):
    post = Post.query.get_or_404(pk)
    if current_user.is_staff or current_user.is_admin:
        post.status = PostStatus.PUBLISHED
        db.session.add(post)
        db.session.commit()
    return redirect(url_for('posts.concrete_post', pk=pk))


@login_required
@posts.route('/comment/<int:comment_id>/update/', methods=['GET', 'POST'])
def update_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    form = UpdateCommentForm()

    if comment.username == current_user.username or current_user.is_admin:
        if request.method == 'GET':
            form.body.data = comment.body

        if form.validate_on_submit():
            comment.body = form.body.data
            db.session.commit()
            return redirect(url_for('posts.concrete_post', pk=comment.post_id))

    return render_template('comment_update.html', form=form)


@login_required
@posts.route('/comment/<int:comment_id>/delete/')
def delete_comment(comment_id):
    remove_comment = Comment.query.get_or_404(comment_id)
    if remove_comment.username == current_user.username or current_user.is_admin:
        db.session.delete(remove_comment)
        db.session.commit()
        return redirect(url_for('posts.concrete_post', pk=remove_comment.post_id))


@posts.route('/like/<int:post_id>/<action>')
@login_required
def like_action(post_id, action):
    post = Post.query.filter_by(id=post_id).first_or_404()
    if action == 'like':
        current_user.like_post(post)
        post.likes += 1
        db.session.commit()
    if action == 'unlike':
        current_user.unlike_post(post)
        post.likes -= 1
        db.session.commit()
    return redirect(request.referrer)
