import PIL
import StringIO
import requests

def main():
    """http://www.pythonchallenge.com/pc/return/5808.html"""
    web_res = urllib.urlopen(r'http://www.pythonchallenge.com/pc/return/cave.jpg')
    f = StringIO.StringIO(web_res.read())
    im = PIL.Image.open(f)



if __name__ == '__main__':
    main()

