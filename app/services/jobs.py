import pymongo
from app.services import hacker_news_api, unbabel_api
from config import TOP_POSTS_LIMIT, LAN_1, LAN_2
from pymongo import MongoClient
from bson.objectid import ObjectId
import threading
import time

def save_hacker_news_posts():
    print "Starting job.."
    client = MongoClient('localhost', 27017)
    db = client['multilingual-hackernews']
    db.new_posts.drop()
    posts = hacker_news_api.get_all_posts(TOP_POSTS_LIMIT)

    start_time = time.time()
    threads = [threading.Thread(target=insert_item, args=(db,post)) for post in posts]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    db.posts.drop()
    db.new_posts.rename('posts')
    print("Job completed: it took %s seconds ---" % (time.time() - start_time))

def insert_item(db,post_id):
    post = hacker_news_api.get_post(str(post_id))
    post_title = post['post_info']['title']
    uid_1 = unbabel_api.post_mt_translation(post_title, LAN_1)
    uid_2 = unbabel_api.post_mt_translation(post_title, LAN_2)
    post['comments'] = fetch_comment_data(post['post_info']['comments'])
    add_translated_titles(post, {LAN_1: uid_1, LAN_2: uid_2})
    db.new_posts.insert_one(post)

def add_translated_titles(post, uids):
    post['post_info']["title-%s"%LAN_1] = unbabel_api.get_mt_translation(uids[LAN_1])
    post['post_info']["title-%s"%LAN_2] = unbabel_api.get_mt_translation(uids[LAN_2])


def fetch_comment_data(comments_ids):
    comments = []
    for comment in comments_ids:
        comments.append(hacker_news_api.get_comment(str(comment)))
    return comments
