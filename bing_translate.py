import websocket
import thread
import json
import requests
import urllib
import wave
import audioop
from time import sleep
import StringIO
import struct
import sys
import codecs
from xml.etree import ElementTree


def get_oauth_token(): #Get the access token from ADM, token is good for 10 minutes
    urlArgs = {
        'client_id': '',
        'client_secret': '',
        'scope': 'http://api.microsofttranslator.com',
        'grant_type': 'client_credentials'
    }

    oauth_url = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'
    final_token = None
    try:
        oauth_token = json.loads(requests.post(oauth_url, data = urllib.urlencode(urlArgs)).content)
        final_token = "Bearer " + oauth_token['access_token']
    except Exception as e:
        print "Error", e

    return final_token

def translate_to_arabic(lines):
    final_token = get_oauth_token()
    for line in lines:
        headers = {"Authorization ": final_token}
        translate_url = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}".format(line, 'ar')
        data = requests.get(translate_url, headers = headers)
        translation = ElementTree.fromstring(data.text.encode('utf-8'))
        print "The translation is---> ", translation.text

if __name__ == '__main__':
    translate_to_arabic(['india is a great country'])

