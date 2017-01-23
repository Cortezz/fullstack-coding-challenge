import httplib
import requests
import json
import code

hacker_news_endpoint = 'https://hacker-news.firebaseio.com/v0/'

def top10_posts():
    response = requests.get(hacker_news_endpoint+'beststories.json').content
    data = json.loads(response)
    return data[:10]
