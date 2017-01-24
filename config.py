import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True

TOP_POSTS_LIMIT = 10

MONGODB_NAME = 'multilingual-hackernews'
MONGO_URI = 'mongodb://localhost:27017/multilingual-hackernews'
