import requests
import json

unbabel_api_endpoint = 'https://sandbox.unbabel.com/tapi/v2/'

headers = {
    'Authorization': 'ApiKey {}:{}'.format(UNBABEL_USER, UNBABEL_API_KEY),
    'Content-Type': 'application/json'
}

def post_mt_translation(text, dest_lang):
    payload = {
        "text": text,
        "target_language": dest_lang
    }
    response = requests.post(unbabel_api_endpoint+'/mt_translation/',
        headers = headers,
        data = json.dumps(payload)
    )
    data = response.json()

    return str(data['uid'])

def get_mt_translation(uid):
    response = requests.get(unbabel_api_endpoint+'/mt_translation/'+uid, headers = headers)
    data = response.json()

    if 'translatedText' in data
        return str(data['translatedText'])
    else
        return "No translation available"
