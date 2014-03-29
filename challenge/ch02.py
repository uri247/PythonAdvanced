import string
from globals import pych_url
from ch02_input import text

def main():
    """http://www.pythonchallenge.com/pc/def/ocr.html"""
    d = {ch: 0 for ch in string.printable}
    for ch in text:
        d[ch] += 1

    avg = len(text) / len(d)
    rare_chars = ''.join([ch for ch, val in d.items() if 0 < val < avg])

    by_appearance = ''.join(sorted(rare_chars, key=lambda c: text.find(c)))

    print by_appearance
    print pych_url(by_appearance)


if __name__ == '__main__':
    main()




