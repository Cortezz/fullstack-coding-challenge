import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True

TOP_POSTS_LIMIT = 10

MONGODB_NAME = 'multilingual-hackernews'
MONGO_URI = 'mongodb://localhost:27017/multilingual-hackernews'

UNBABEL_USER = 'backendchallenge'
UNBABEL_API_KEY = '711b8090e84dcb4981e6381b59757ac5c75ebb26'

LAN_1 = 'fr'
LAN_2 = 'it'
