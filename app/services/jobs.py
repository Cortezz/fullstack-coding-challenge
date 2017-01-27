import threading
import time

from app.services import hacker_news_api, unbabel_api, mongo
from app.models import post, translation
from config import TOP_POSTS_LIMIT, LAN_1, LAN_2

def save_hacker_news_posts():
    print "Starting job.."
    top_posts = hacker_news_api.get_all_posts(TOP_POSTS_LIMIT)
    empty_collection = mongo.collection_empty('posts')
    new_posts = []


    start_time = time.time()
    threads = [threading.Thread(target=insert_post, args=(post_id, new_posts, empty_collection)) for post_id in top_posts]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    if not empty_collection:
        post.delete_all()
    post.save_all(new_posts)
    print("Job completed: it took %s seconds ---" % (time.time() - start_time))

def insert_post(post_id, new_posts, empty_collection):
    if not empty_collection:
        old_post = post.get(str(post_id))
        if not old_post:
            new_post = insert_new_post(post_id)
        else:
            new_post = update_old_post(old_post)
    else:
        new_post = insert_new_post(post_id)
    new_posts.append(new_post)

def insert_new_post(post_id):
    print "About to look for a new post - #%s"% post_id
    new_post = hacker_news_api.get_post(str(post_id))
    post_title = new_post['title']
    uid_1 = unbabel_api.post_mt_translation(post_title, LAN_1)
    uid_2 = unbabel_api.post_mt_translation(post_title, LAN_2)
    if 'comments' in new_post:
        new_post['comments'] = fetch_comment_data(new_post['comments'])
    add_translated_titles(new_post, {LAN_1: uid_1, LAN_2: uid_2})
    return new_post

def update_old_post(old_post):
    print "Updating an old post - #%s"% old_post['id']

    old_comments = []
    updated_post = hacker_news_api.get_post(old_post['id'])
    for old_comment in old_post['comments']:
        if old_comment:
            old_comments.append(str(old_comment['id']))

    updated_post['comments'] = [str(comment) for comment in updated_post['comments']]
    updated_comments = list(set(updated_post['comments']) - set(old_comments))

    new_comments = fetch_comment_data(updated_comments)
    if new_comments:
        print "Adding new comments to post #%s"%old_post['id']
        for new_comment in new_comments:
            old_post['comments'].append(new_comment)
    return old_post

def add_translated_titles(post, uids):
    for language, uid in uids.iteritems():
        machine_translation = unbabel_api.get_mt_translation(uid)
        if machine_translation['status'] == 'completed':
            post["title_%s"%language] = machine_translation['text']
        else:
            print "Unbabel polling job goes here"
        machine_translation['post_id'] = post['id']
        translation.save(machine_translation)

def fetch_comment_data(comments_ids):
    comments = []
    for c in comments_ids:
        comment = hacker_news_api.get_comment(str(c))
        if comment:
            comments.append(comment)
    return comments


def unbabel_translation_polling():
    print "Unbabel polling..."
    translations = translation.get_by_not_status('completed')
    unfinished_translations = []

    start_time = time.time()
    threads = [threading.Thread(target=update_translation,
        args=(t, unfinished_translations)) for t in translations
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    if len(unfinished_translations) == 0:
        print "No unfinished translations!"
    print("Polling completed: it took %s seconds ---" % (time.time() - start_time))

def update_translation(trans, unfinished_translations):
    machine_translation = unbabel_api.get_mt_translation(trans['uid'])
    if machine_translation['status'] == 'completed':
        trans['status'] = 'completed'
        trans['translated_text'] = machine_translation['translated_text']
        translation.update(trans)
        p = post.get(trans['post_id'])
        p['title_%s'%trans['target_language']] = machine_translation['translated_text']
        post.update(p)
    else:
        unfinished_translations.append(translation['uid'])
