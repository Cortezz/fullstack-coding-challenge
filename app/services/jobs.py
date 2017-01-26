from app.services import hacker_news_api, unbabel_api, mongo
from app.models import post, translation
from config import TOP_POSTS_LIMIT, LAN_1, LAN_2
from bson.objectid import ObjectId
import threading
import time

def save_hacker_news_posts():
    print "Starting job.."
    posts = hacker_news_api.get_all_posts(TOP_POSTS_LIMIT)
    new_posts = []
    start_time = time.time()
    threads = [threading.Thread(target=insert_post, args=(p,new_posts)) for p in posts]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    if not mongo.collection_empty('posts'):
        post.delete_all()
    post.save_all(new_posts)
    print("Job completed: it took %s seconds ---" % (time.time() - start_time))

def insert_post(post_id, new_posts):
    post = hacker_news_api.get_post(str(post_id))
    post_title = post['title']
    uid_1 = unbabel_api.post_mt_translation(post_title, LAN_1)
    uid_2 = unbabel_api.post_mt_translation(post_title, LAN_2)
    post['comments'] = fetch_comment_data(post['comments'])
    add_translated_titles(post, {LAN_1: uid_1, LAN_2: uid_2})
    new_posts.append(post)

def add_translated_titles(post, uids):
    for language, uid in uids.iteritems():
        machine_translation = unbabel_api.get_mt_translation(uid)
        if 'text' in machine_translation:
            post["title_%s"%language] = machine_translation['text']
        else:
            print "Unbabel polling job goes here"
        translation.save(machine_translation)

def fetch_comment_data(comments_ids):
    comments = []
    for comment in comments_ids:
        comments.append(hacker_news_api.get_comment(str(comment)))
    return comments
