#!env/bin/python
from app import app
from apscheduler.schedulers.background import BackgroundScheduler
from app.jobs import fetch_hacker_news_posts, unbabel_polling
import logging


#use_reloader = False
scheduler = BackgroundScheduler()
logging.basicConfig()
scheduler.add_job(fetch_hacker_news_posts.perform, 'interval', minutes=5)
scheduler.add_job(unbabel_polling.perform, 'interval', seconds=20)
scheduler.start()

app.run(debug=True, use_reloader=False)
