from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app.services import hacker_news
from config import TOP_POSTS_LIMIT


posts = Blueprint('posts', __name__, url_prefix='/posts')

@posts.route('/')
def index():
    posts = hacker_news.get_all(TOP_POSTS_LIMIT)
    return render_template('posts/index.html', posts=posts)

@posts.route('/<post_id>')
def show(post_id):
    post = hacker_news.get(post_id)
    return render_template('posts/show.html', post=post)
