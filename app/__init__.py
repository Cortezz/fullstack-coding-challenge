from flask import Flask, render_template
from flask_pymongo import PyMongo
from apscheduler.schedulers.background import BackgroundScheduler
from app.services.background_jobs import save_posts


scheduler = BackgroundScheduler()
scheduler.add_job(save_posts, 'cron', second='*/520')
scheduler.start()

app = Flask(__name__)
app.config.from_object('config')
mongo = PyMongo(app)


from app.controllers.posts_controller import posts

app.register_blueprint(posts)
