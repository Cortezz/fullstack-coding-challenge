import httplib
import requests
import json

hacker_news_endpoint = 'https://hacker-news.firebaseio.com/v0/'

def get_all(limit):
    response = requests.get(hacker_news_endpoint+'beststories.json').content
    data = json.loads(response)
    return data[:limit]

def get(post_id):
    response = requests.get(hacker_news_endpoint+'item/'+post_id+'.json').content
    data = json.loads(response)
    return {
        'id': post_id,
        'post_info': {
            'title': data['title'],
            'score': data['score'],
            'comments': data['kids'],
            'author': data['by']
        }
    }
