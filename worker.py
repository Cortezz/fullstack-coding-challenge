from apscheduler.schedulers.background import BackgroundScheduler
from app.services.jobs import save_hacker_news_posts


scheduler = BackgroundScheduler()
scheduler.add_job(save_hacker_news_posts, 'cron', second='*/520')
scheduler.start()
