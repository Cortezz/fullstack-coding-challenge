from app import db

def get_all():
    return db.posts.find({})

def get(post_id):
    return db.posts.find_one({'id': post_id})

def save(post):
    db.posts.insert_one(post)

def save_all(posts):
    db.posts.insert_many(posts)

def delete_all():
    db.posts.delete_many({})
