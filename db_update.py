#!env/bin/python
from app.jobs import fetch_hacker_news_posts

fetch_hacker_news_posts.perform()
