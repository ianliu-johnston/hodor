#!/usr/bin/python
from PIL import Image
import urllib, urllib2
from time import sleep

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
        'key': "fdbbcf4d5e84d891b52f844651ea62d47f12cb86", \
        'holdthedoor': "Submit", \
        'captcha': '0'}

def request(url, captcha):
    try:
        oc = ocr(captcha)
        cap = {'captcha': oc}
        post_data.update(cap)
        data = urllib.urlencode(post_data)
        print (data)
    except Exception as e:
        print (e)
        raise
    try:
        c = urllib2.Request(url, data, headers)
        c.request('POST', url, data, headers)
        c.close()
    except Exception as e:
        print (e)
        raise
    return (urllib2.urlopen(c).read())

def ocr(im, threshold=200, mask="letters.bmp", alphabet="0123456789abcdefghijklmnopqrstuvwxyz"):
    img = Image.open(im)
    img = img.convert("RGB")
    box = (8, 8, 58, 18)
    img = img.crop(box)
    pixdata = img.load()

    #open mask
    letters = Image.open(mask)
    ledata = letters.load()

    def test_letter(img, letter):
        A = img.load()
        B = letter.load()
        mx = 1000000
        max_x = 0
        x = 0
        for x in range(img.size[0] - letter.size[0]):
            _sum = 0
            for i in range(letter.size[0]):
                for j in range(letter.size[1]):
                    _sum = _sum + abs(A[x + i, j][0] - B[i, j][0])
                if _sum < mx:
                    mx = _sum
                    max_x = x
        return (mx, max_x)

    #clean bkg noise. is color != white, set to black
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if (pixdata[x, y][0] > threshold) and (pixdata[x, y][1] > threshold) and (pixdata[x, y][2] > threshold):
                pixdata[x, y] = (255, 255, 255, 255)
            else:
                pixdata[x, y] = (0, 0, 0, 0)

    counter = 0
    old_x = -1

    letterlst = []

    for x in range(letters.size[0]):
        black = True
        for y in range(letters.size[1]):
            if ledata[x, y][0] != 0:
                black = False
                break
        if black:
            if True:
                box = (old_x + 1, 0, x, 10)
                letter = letters.crop(box)
                t = test_letter(img, letter)
                letterlst.append((t[0], alphabet[counter], t[1]))
            old_x = x
            counter += 1

    box = (old_x + 1, 0, 140, 10)
    letter = letters.crop(box)
    t = test_letter(img, letter)
    letterlst.append((t[0], alphabet[counter], t[1]))

    t = sorted(letterlst)
    t = t[0:4] # 4 letter captcha

    final = sorted(t, key=lambda e: e[2])

    answer = ''.join(map(lambda l: l[1], final))
    return answer

if __name__ == "__main__":
    try:
        raw = urllib.urlretrieve("http://54.221.6.249/captcha.php", "tmp.png")
    except Exception as e:
        print(e)
        raise
    with open("tmp.png", 'rb') as c:
        request("http://54.221.6.249/level3.php", c)
