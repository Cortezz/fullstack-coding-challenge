from flask_pymongo import PyMongo
from app import mongo
import code


def get_all():
    return mongo.db.stories.find({})

def get(post_id):
    return mongo.db.stories.find_one({'id': post_id})
