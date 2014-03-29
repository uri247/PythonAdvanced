import re


def main():
    """http://www.pythonchallenge.com/pc/return/bull.html
    http://www.pythonchallenge.com/pc/return/sequence.txt"""

    rx = re.compile(r'(.)\1*')
    s = '1'

    for _i in range(30):
        s = ''.join([str(len(m.group())) + m.group()[0] for m in rx.finditer(s)])

    print len(s)
    print r'http://www.pythonchallenge.com/pc/return/5808.html'

if __name__ == '__main__':
    main()

