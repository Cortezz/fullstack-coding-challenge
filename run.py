#!env/bin/python
from app import app
from apscheduler.schedulers.background import BackgroundScheduler
from app.services.jobs import save_hacker_news_posts, unbabel_translation_polling
import logging


#use_reloader = False
scheduler = BackgroundScheduler()
logging.basicConfig()
scheduler.add_job(save_hacker_news_posts, 'interval', minutes=5)
scheduler.add_job(unbabel_translation_polling, 'interval', seconds=20)
scheduler.start()

app.run(debug=True, use_reloader=False)
