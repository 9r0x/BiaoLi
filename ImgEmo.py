import requests
import json
from picamera import PiCamera

# pathToFileInDisk = r'/Users/grox/Desktop/image.jpg'

def imgemo():
    camera = PiCamera()
    camera.resolution = (320, 240)
    camera.capture('foo.jpg')
    with open(r'./foo.jpg', 'rb') as f:
        data = f.read()
    _url = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'
    headers = dict()
    headers['Ocp-Apim-Subscription-Key'] = 'd0a8f08cabe04bcfaec68c1b2524a2d1'
    headers['Content-Type'] = 'application/octet-stream'
    json = None
    params = None

    response = requests.request( 'post', _url, json = json, data = data, headers = headers, params = params )
    response = response.json()[0]["scores"]["happiness"]-(response.json()[0]["scores"]["sadness"]+response.json()[0]["scores"]["contempt"]+response.json()[0]["scores"]["disgust"]+response.json()[0]["scores"]["anger"]+ response.json()[0]["scores"]["fear"])/5
    return response
