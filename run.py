#!env/bin/python
from app import app
from app.services.background_jobs import save_posts
#from apscheduler.schedulers.background import BackgroundScheduler


app.run(debug=True, use_reloader=False)
