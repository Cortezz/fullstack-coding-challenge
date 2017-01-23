from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for


posts = Blueprint('posts', __name__, url_prefix='/posts')

@posts.route('/')
def index():
    posts = [  #
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('posts/index.html', posts=posts)
