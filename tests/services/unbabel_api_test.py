import os
import unittest

from app import app
from app.services import unbabel_api

class UnbabelAPITestCase(unittest.TestCase):

    def SetUp(self):
        self.app = app.test_client()

    def test_post_mt_translation(self):
        uid = unbabel_api.post_mt_translation("look", "pt")
        self.assertTrue(uid)

    def test_get_mt_translation(self):
        uid = unbabel_api.post_mt_translation("look", "pt")
        data = unbabel_api.get_mt_translation(uid)
        self.assertTrue('status' in data)
