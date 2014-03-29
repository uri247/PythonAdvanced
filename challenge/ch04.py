from globals import pych_url
import urllib
import re

def nothing_url(nothing):
    return 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={0}'.format(nothing)

def main():
    """http://www.pythonchallenge.com/pc/def/linkedlist.html"""

    rx = re.compile('next nothing is (\d+)$')
    nothing = 12345
    #nothing = 3875
    #nothing = 82682
    #nothing = 66831

    while nothing:
        resource = urllib.urlopen(nothing_url(nothing))
        line = ''.join([l.rstrip() for l in resource.readlines()])
        print line
        match = rx.search(line)
        if match:
            nothing = match.group(1)
        elif re.search('Divide by two and keep going', line):
            nothing = int(nothing) / 2
        else:
            nothing = 0

    print pych_url(line,suffix=False)

if __name__ == '__main__':
    main()
