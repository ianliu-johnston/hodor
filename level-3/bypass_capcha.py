#!/usr/bin/python
from PIL import Image
import pytesseract
import urllib, urllib2
from time import sleep


headers = {'Host': "54.221.6.249", 'User-Agent': "Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0", 'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 'Accept-Language': "en-US,en;q=0.5", 'Referer': "http://54.221.6.249/level4.php", 'Cookie': "PHPSESSID=448qvkqgi0llp0rcq24vkvkfs0; HoldTheDoor=fdbbcf4d5e84d891b52f844651ea62d47f12cb86", 'Connection': "keep-alive"}

data = urllib.urlencode({'id': 28, 'holdthedoor': "Submit+Query", 'key': "fdbbcf4d5e84d891b52f844651ea62d47f12cb86"})

def request(method, post_data, url):
    try:
        c = urllib2.Request(url, post_data, headers)
        c.request(method, url, post_data, headers)
        c.close()
    except Exception as e:
        print (e)
        pass

def get_text(img):
    if not isinstance(img, str):
        raise ValueError
    try:
        im = Image('capcha.php', cv.CL_LOAD_IMAGE_GREYSCALE)
    except Exception as e:
        print (e)
        raise

if __name__ == "__main__":
    try:
        get_text(urllib.urlretrieve("http://54.221.6.249/capcha.php"))
    except Exception as e:
        print (e)
        pass
