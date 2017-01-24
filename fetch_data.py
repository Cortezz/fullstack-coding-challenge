#!env/bin/python
import pymongo
from app.services import hacker_news
from config import TOP_POSTS_LIMIT
from pymongo import MongoClient
import threading
import time

def save_posts():
    db = get_db()
    json = {}
    post_list = []
    posts = hacker_news.get_all_posts(TOP_POSTS_LIMIT)
    threads = [threading.Thread(target=insert_post, args=(db,post)) for post in posts]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

def insert_post(db,post_id):
    post = hacker_news.get_post(str(post_id))
    print "Fetching comments for %s" % str(post_id)
    post['comments'] = fetch_comment_data(post['post_info']['comments'])
    db.stories.insert_one(post)

def fetch_comment_data(comments_ids):
    comments = []
    for comment in comments_ids:
        comments.append(hacker_news.get_comment(str(comment)))
    return comments

def get_db():
    client = MongoClient('localhost', 27017)
    db = client['multilingual-hackernews']
    return db

start = time.time()
save_posts()
print "Time elapsed: %s" % (time.time() - start)
