from flask import Blueprint, render_template
from app.models import post

posts = Blueprint('posts', __name__, url_prefix='/posts')

@posts.route('/')
def index():
    posts = post.get_all()
    return render_template('posts/index.html', posts=posts)

@posts.route('/<post_id>')
def show(post_id):
    p = post.get(post_id)
    return render_template('posts/show.html', post=p)
