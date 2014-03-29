import webapp2
import chat
import pkgs

application = webapp2.WSGIApplication([
    ('/', chat.ChatHandler),
    ('/say', chat.SayHandler),

    ('/pkgs', pkgs.PkgsHandler),

], debug=True)
