#!/usr/bin/python3
from PIL import Image
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
