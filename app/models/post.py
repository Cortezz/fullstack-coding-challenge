from app import db
import code

def get_all():
    return db.posts.find({}).sort('score',-1)

def get(post_id):
    return db.posts.find_one({'id': post_id})

def save(collection, post):
    db[collection].insert_one(post)
