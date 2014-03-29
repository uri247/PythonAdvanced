#! /usr/bin/env python

def application(environ, start_response):
    """This is the application method. It can be name anything, but the canonical name is
    'application'
    :param environ:
    :param start_response:
    :return: an iterator with all the content
    """

    status = '200 OK'
    response_header = [
        ('Content-Type', 'text/html'),
    ]
    start_response(status, response_header)

    yield '<html><head></head><body>'
    yield '<table>'
    for key, value in sorted(environ.items()):
        yield '<tr><td>%s</td><td>%s</td></tr>' % (key, value)
    yield '</table>'
    yield '</body></html>'

