#!env/bin/python
import os
import unittest

from config import TOP_POSTS_LIMIT
from app import app
from app.services import hacker_news


class HackerNewsTestCase(unittest.TestCase):
    def SetUp(self):
        self.app = app.test_client()


    def TearDown(self):
        print "clears test DB"

    def test_get_all(self):
        posts = hacker_news.get_all(TOP_POSTS_LIMIT)
        assert len(posts) == TOP_POSTS_LIMIT

    def test_get(self):
        posts = hacker_news.get_all(TOP_POSTS_LIMIT)
        post = hacker_news.get(str(posts[0]))
        self.assertTrue(post['author'])
        self.assertTrue(post['title'])
        self.assertTrue(post['score'])

if __name__ == '__main__':
    unittest.main()
