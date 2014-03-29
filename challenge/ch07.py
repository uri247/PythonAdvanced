import PIL.Image
import urllib
import StringIO
import re
from globals import pych_url


def main():
    """http://www.pythonchallenge.com/pc/def/oxygen.html"""
    web_res = urllib.urlopen(pych_url('oxygen.png', False))
    f = StringIO.StringIO(web_res.read())

    im = PIL.Image.open(f)
    width, height = im.size
    x = 2
    text = ''
    ords = []
    while x < width:
        r, g, b, a = im.getpixel((x, height/2))
        if not r == g == b:
            break
        x += 7
        ords.append(r)
    text = ''.join(chr(ord) for ord in ords)
    print text
    arr_text = text[text.index('[')+1:text.index(']')]
    target = ''.join([chr(int(n)) for n in arr_text.split(', ')])
    print target
    print pych_url(target)

if __name__ == '__main__':
    main()

