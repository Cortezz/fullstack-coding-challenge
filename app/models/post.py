from flask_pymongo import PyMongo
from app import mongo
import code


def get_all():
    return mongo.db.posts.find({}).sort('score',-1)

def get(post_id):
    return mongo.db.posts.find_one({'id': post_id})
