from globals import pych_url
from string import maketrans


def main():
    """solution for http://www.pythonchallenge.com/pc/def/map.html"""
    text = """
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm
jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

    letters = 'abcdefghijklmnopqrstuvwxyz'
    to = letters[2:] + letters[:2]

    trans = maketrans(letters, to)
    clear = text.translate(trans)

    print clear

    base = 'map'.translate(trans)
    print base
    print pych_url(base)


if __name__ == '__main__':
    main()
