from app.services import hacker_news_api, unbabel_api, mongo
from app.models import post
from config import TOP_POSTS_LIMIT, LAN_1, LAN_2
from bson.objectid import ObjectId
import threading
import time

def save_hacker_news_posts():
    print "Starting job.."
    mongo.delete_collection('new_posts')
    posts = hacker_news_api.get_all_posts(TOP_POSTS_LIMIT)

    start_time = time.time()
    threads = [threading.Thread(target=insert_post, args=(p,)) for p in posts]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    mongo.delete_collection('posts')
    mongo.rename_collection('new_posts','posts')
    print("Job completed: it took %s seconds ---" % (time.time() - start_time))

def insert_post(post_id):
    p = hacker_news_api.get_post(str(post_id))
    post_title = p['title']
    uid_1 = unbabel_api.post_mt_translation(post_title, LAN_1)
    uid_2 = unbabel_api.post_mt_translation(post_title, LAN_2)
    p['comments'] = fetch_comment_data(p['comments'])
    add_translated_titles(p, {LAN_1: uid_1, LAN_2: uid_2})
    post.save('new_posts', p)

def add_translated_titles(post, uids):
    post["title_%s"%LAN_1] = unbabel_api.get_mt_translation(uids[LAN_1])
    post["title_%s"%LAN_2] = unbabel_api.get_mt_translation(uids[LAN_2])


def fetch_comment_data(comments_ids):
    comments = []
    for comment in comments_ids:
        comments.append(hacker_news_api.get_comment(str(comment)))
    return comments
