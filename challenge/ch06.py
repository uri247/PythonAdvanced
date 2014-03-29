import zipfile
import urllib
import tempfile
import re
import os
from globals import pych_url


def download_zipfile():
    # get the zip resource from the web
    web_res = urllib.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip')

    #save to file
    f = tempfile.TemporaryFile()
    f.write(web_res.read())

    #load to zip file
    zf = zipfile.ZipFile(f)
    return zf



def main():
    """http://www.pythonchallenge.com/pc/def/channel.html"""

    zf = download_zipfile()
    comments = []

    #read the readme file
    readme = zf.read('readme.txt')
    nothing = re.search('hint1: start from (\d+)', readme).group(1)
    print 'start: {start}'.format(start=nothing)

    while nothing:
        fname = nothing + '.txt'
        info = zf.getinfo(fname)
        comment = info.comment
        content = zf.read(fname)
        print '{fname}: {comment} - {content}'.format(fname=fname, comment=comment, content=content)
        comments.append(comment)

        result = re.search('nothing is (\d+)$', content)
        if result:
            nothing = result.group(1)
        else:
            nothing = 0

    print ''.join(comments)
    print pych_url('hockey')
    print pych_url('oxygen')


if __name__ == '__main__':
    main()

