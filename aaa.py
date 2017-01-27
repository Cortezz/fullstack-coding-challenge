#!env/bin/python
from app.models import post
from app.services.jobs import insert_post
from app.services import hacker_news_api

top_posts = hacker_news_api.get_all_posts(10)
new_posts=[]
for post in top_posts:
    insert_post(post, new_posts, False)
