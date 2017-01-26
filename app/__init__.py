from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object('config')

client = MongoClient('localhost', 27017)
db = client['multilingual-hackernews']
#mongo = PyMongo(app)

from app.controllers.posts_controller import posts
from app.controllers.translations_controller import translations
from app.controllers.dashboard_controller import dashboard

app.register_blueprint(dashboard)
app.register_blueprint(translations)
app.register_blueprint(posts)
