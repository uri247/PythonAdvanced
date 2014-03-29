import re
from globals import pych_url
from ch03_input import text

def main():
    """http://www.pythonchallenge.com/pc/def/equality.html"""
    clean_text = re.sub('\s', '', text)
    all = re.findall('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', text)
    result = ''.join([res[4] for res in all])
    print result
    print pych_url(result)


if __name__ == '__main__':
    main()
