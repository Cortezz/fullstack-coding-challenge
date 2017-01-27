import os
import unittest

from config import TOP_POSTS_LIMIT
from app import app
from app.services import hacker_news_api

class HackerNewsAPITestCase(unittest.TestCase):
    
    def SetUp(self):
        self.app = app.test_client()

    def TearDown(self):
        print "clears test DB"

    def test_get_all(self):
        posts = hacker_news_api.get_all_posts(TOP_POSTS_LIMIT)
        assert len(posts) == TOP_POSTS_LIMIT

    def test_get(self):
        posts = hacker_news_api.get_all_posts(TOP_POSTS_LIMIT)
        post = hacker_news_api.get_post(str(posts[0]))
        self.assertTrue(post['author'])
        self.assertTrue(post['title'])
        self.assertTrue(post['score'])
