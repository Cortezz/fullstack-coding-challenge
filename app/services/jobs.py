import pymongo
from app.services import hacker_news_api, unbabel_api
from config import TOP_POSTS_LIMIT, COLLECTION_NAME, NEW_COLLECTION_NAME
from pymongo import MongoClient
from bson.objectid import ObjectId
import threading
import time

def save_hacker_news_posts():
    print "Starting job.."
    client = MongoClient('localhost', 27017)
    db = client['multilingual-hackernews']
    db[NEW_COLLECTION_NAME].drop()
    items = hacker_news_api.get_all_posts(TOP_POSTS_LIMIT)

    start_time = time.time()
    threads = [threading.Thread(target=insert_item, args=(db,post)) for item in items]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    db[COLLECTION_NAME].drop()
    db[NEW_COLLECTION_NAME].rename(COLLECTION_NAME)
    print("Job completed: it took %s seconds ---" % (time.time() - start_time))

def insert_item(db,post_id):
    post = hacker_news_api.get_post(str(post_id))
    post['comments'] = fetch_comment_data(post['post_info']['comments'])
    db[NEW_COLLECTION_NAME]insert_one(post)

def fetch_comment_data(comments_ids):
    comments = []
    for comment in comments_ids:
        comments.append(hacker_news_api.get_comment(str(comment)))
    return comments
