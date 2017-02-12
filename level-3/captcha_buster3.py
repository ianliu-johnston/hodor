#!/usr/bin/python

import urllib2
from PIL import Image
import pytesseract
from ocr import ocr


headers = {\
        'Host': "54.221.6.249", \
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0", \
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", \
        'Accept-Language': "en-US,en;q=0.5", \
        'Referer': "http://54.221.6.249/level3.php", \
        'Cookie': "0", \
        'Connection': "keep-alive", \
        'Upgrade-Insecure-Requests': "1"}

post_data = {\
        'id': 53, \
        'key': 0, \
        'holdthedoor': "Submit", \
        'captcha': 0}

url = "http://54.221.6.249/level3.php"

def request(method, url, data):
    data = urllib2.urlencode(post_data)
    try:
        c = urllib2.Request(url, data, headers)
        c.request(method, url, data, headers)
        c.close()
    except Exception as e:
        print(e)
        raise
    return(urllib2.urlopen(c).read())

if __name__ == "__main__":
    try:
        data = None
        get = request("GET", url, data)
        data = urllib2.urlencode(post_data)
