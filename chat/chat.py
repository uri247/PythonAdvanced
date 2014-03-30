import webapp2
import cgi
from google.appengine.api import users
from google.appengine.ext import ndb
from globals import JINJA_ENVIRONMENT, DEFAULT_ROOM_NAME


class Message(ndb.Model):
    author = ndb.UserProperty()
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)


class ChatHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            self.response.headers['Content-Type'] = 'text/html'
            payload = JINJA_ENVIRONMENT.get_template('chat.html').render({
                'room_name': DEFAULT_ROOM_NAME,
                'user_name': user.nickname(),
            })
            self.response.write(payload)

        else:
            self.redirect(users.create_login_url(self.request.uri))


class SayHandler(webapp2.RequestHandler):
    def post(self):
        room_name = self.request.get('room_name', DEFAULT_ROOM_NAME)
        key = ndb.Key('Room', room_name)
        message = Message(parent=key)
        message.author = users.get_current_user()
        message.content = cgi.escape(self.request.get('content'))
        message.put()

        self.response.write('You said:')
        self.response.write(cgi.escape(self.request.get('content')))
