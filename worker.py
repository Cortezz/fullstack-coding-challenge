from apscheduler.schedulers.background import BackgroundScheduler
from app.services.jobs import save_hacker_news_posts


scheduler = BackgroundScheduler()
scheduler.add_job(save_hacker_news_posts, 'interval', minutes=4)
scheduler.start()
