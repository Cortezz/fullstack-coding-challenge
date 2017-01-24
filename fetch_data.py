#!env/bin/python
import pymongo
from app.services import hacker_news
from config import TOP_POSTS_LIMIT
from pymongo import MongoClient

def save_posts():
    db = get_db()
    json = {}
    post_list = []
    posts = hacker_news.get_all(TOP_POSTS_LIMIT)
    for post in posts:
        p = hacker_news.get(str(post))
        db.stories.insert_one(p)


def get_db():
    client = MongoClient('localhost', 27017)
    db = client['multilingual-hackernews']
    collection = db['stories']
    return db

save_posts()
