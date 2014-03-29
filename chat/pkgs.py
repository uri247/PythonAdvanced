import webapp2
import pkgutil
import sys
import cgi
from globals import JINJA_ENVIRONMENT


class Package(object):
    def __init__(self, pkg):
        self.name = pkg[1]
        self.path = pkg[0].path
        self.package = pkg[2]
        try:
            self.succeed = False
            mod = __import__(self.name)
            self.succeed = True
            self.doc = cgi.escape(mod.__doc__).replace('\n', '<br>')
        except BaseException as x:
            self.doc = repr(x)


class PkgsHandler(webapp2.RequestHandler):
    def get(self):
        pkgs = [Package(pkg) for pkg in pkgutil.iter_modules()]
        self.response.headers['Content-Type'] = 'text/html'
        payload = JINJA_ENVIRONMENT.get_template('pkgs.html').render({
            'pkgs': pkgs
        })
        self.response.write(payload)
