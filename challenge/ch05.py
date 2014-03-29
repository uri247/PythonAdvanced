import urllib
import pickle
from globals import pych_url

def main():
    """http://www.pythonchallenge.com/pc/def/peak.html
    http://www.pythonchallenge.com/pc/def/pickle.html"""

    stream = urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
    obj = pickle.load(stream)
    for line in obj:
        print ''.join(e[0] * e[1] for e in line)
    print pych_url('channel')

if __name__ == '__main__':
    main()
