import httplib
import requests
import json
import code

from lib import time_conversion

hacker_news_endpoint = 'https://hacker-news.firebaseio.com/v0/'

def get_all_posts(limit):
    response = requests.get(hacker_news_endpoint+'topstories.json').content
    data = json.loads(response)
    return data[:limit]

def get_post(post_id):
    response = requests.get(hacker_news_endpoint+'item/'+post_id+'.json').content
    data = json.loads(response)

    if 'kids' in data:
        return {
            'id': post_id,
            'title': data['title'],
            'score': data['score'],
            'comments': data['kids'],
            'author': data['by'],
            'time': time_conversion.unix_time_to_string(data['time'])
        }
    else:
     return {
        'id': post_id,
        'title': data['title'],
        'score': data['score'],
        'author': data['by'],
        'time': time_conversion.unix_time_to_string(data['time'])
    }

def get_comment(comment_id):
    response = requests.get(hacker_news_endpoint+'item/'+comment_id+'.json').content
    data = json.loads(response)

    if 'deleted' not in data:
        return {
            'id': comment_id,
            'author': data['by'],
            'text': data['text'],
            'time': time_conversion.unix_time_to_string(data['time'])
        }
