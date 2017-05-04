import requests
import json

def textemo(sentence):
    _url = "https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment"
    headers = dict()
    headers['Content-Type'] = 'application/json'
    headers['Ocp-Apim-Subscription-Key'] = 'a623b7dead114a72bf06d78855fa8b16'

    json = {"documents": [{"language": "en","id": "1","text": sentence}]}
    params = None
    data = None

    response = requests.request( 'post', _url, json = json, headers = headers, params = params )
    return response.json()["documents"][0]["score"]
