from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')

from app.controllers.posts_controller import posts

app.register_blueprint(posts)
