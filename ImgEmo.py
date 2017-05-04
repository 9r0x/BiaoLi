import requests
import json
# pathToFileInDisk = r'/Users/grox/Desktop/image.jpg'

def imgemo(path):
    with open( path, 'rb' ) as f:
        data = f.read()
    _url = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'
    headers = dict()
    headers['Ocp-Apim-Subscription-Key'] = 'd0a8f08cabe04bcfaec68c1b2524a2d1'
    headers['Content-Type'] = 'application/octet-stream'
    json = None
    params = None

    response = requests.request( 'post', _url, json = json, data = data, headers = headers, params = params )

    return response.json()[0]["scores"]
