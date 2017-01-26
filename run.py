#!env/bin/python
from app import app
from apscheduler.schedulers.background import BackgroundScheduler
from app.services.jobs import save_hacker_news_posts


#use_reloader = False

scheduler = BackgroundScheduler()
scheduler.add_job(save_hacker_news_posts, 'interval', minutes=5)
scheduler.start()

app.run(debug=True, use_reloader=False)
