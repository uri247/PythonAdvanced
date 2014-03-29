
def pych_url(base, suffix=True):
    if suffix:
        return 'http://www.pythonchallenge.com/pc/def/{base}.html'.format(base=base)
    else:
        return 'http://www.pythonchallenge.com/pc/def/{base}'.format(base=base)
