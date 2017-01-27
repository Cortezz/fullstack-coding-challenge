import httplib
import requests
import json

hacker_news_endpoint = 'https://hacker-news.firebaseio.com/v0/'

def get_all_posts(limit):
    response = requests.get(hacker_news_endpoint+'topstories.json').content
    data = json.loads(response)
    return data[:limit]

def get_post(post_id):
    response = requests.get(hacker_news_endpoint+'item/'+post_id+'.json').content
    data = json.loads(response)
    return {
        'id': post_id,
        'title': data['title'],
        'score': data['score'],
        'comments': data['kids'],
        'author': data['by']
    }

def get_comment(comment_id):
    response = requests.get(hacker_news_endpoint+'item/'+comment_id+'.json').content
    data = json.loads(response)
    if 'deleted' not in data:
        return {
            'id': comment_id,
            'author': data['by'],
            'text': data['text']
        }
