import webapp2
import chat
import pkgs


class IndexHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect('/chat')



application = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/chat', chat.ChatHandler),
    ('/say', chat.SayHandler),

    ('/pkgs', pkgs.PkgsHandler),

], debug=True)
