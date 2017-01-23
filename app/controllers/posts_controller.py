from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app.services.hacker_news import top10_posts


posts = Blueprint('posts', __name__, url_prefix='/posts')

@posts.route('/')
def index():
    posts = top10_posts()
    return render_template('posts/index.html', posts=posts)
