import os
import unittest
from mock import MagicMock
from mock import patch
from pymongo import MongoClient
import json
import code
import copy

from app.jobs import fetch_hacker_news_posts
from app.services import hacker_news_api, mongo




class FetchHackerNewsPostsTestCase(unittest.TestCase):
    client = MongoClient('localhost', 27017)
    db = client['multilingual-hackernews_test']


    def SetUp(self):
        self.app = app.test_client()

    def TearDown(self):
        MongoClient('localhost', 27017).drop_database('multilingual-hackernews_test')

    @patch('app.services.hacker_news_api.get_comment')
    def test_fetch_comment_data(self, mock_get_comment):
        mock_get_comment.return_value = {
            'id': 1,
            'author': "Special Juan",
            'text': "I zink i'm a special juan"
        }

        comments = fetch_hacker_news_posts.fetch_comment_data([1,2,3,4])
        assert len(comments) == 4

    def test_fetch_comment_data_empty(self):
        comments = fetch_hacker_news_posts.fetch_comment_data([])
        assert not comments

    @patch('app.services.hacker_news_api.get_post')
    @patch('app.jobs.fetch_hacker_news_posts.fetch_comment_data')
    def test_update_old_post(self, comments_mock, updated_post_mock):
        old_post = {
            "title" : "Comparing Elixir and Go",
            "author" : "iamd3vil",
            "comments" : [ { "text": "what", "id" : "13500984",  "author" : "pmarreck"}],
            "title_fr" : "Comparaison Elixir and Go",
            "score" : 374,
            "title_it" : "Confrontando Elixir and Go",
            "id" : "13497505"
        }
        updated_post = copy.deepcopy(old_post)
        updated_post['comments'] = [13500984, 1123412]
        updated_post_mock.return_value = updated_post
        comments_mock.return_value = [{"text": "aaaaaa", "id": "1123412", "author": "420blazeit"}]

        new_post = fetch_hacker_news_posts.update_old_post(old_post)
        assert len(new_post['comments']) == 2

    
