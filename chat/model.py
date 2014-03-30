from google.appengine.ext import ndb


class MessageModel(ndb.Model):
    author = ndb.UserProperty()
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)


class ChatterModel(ndb.Model):
    """model an individual user currently connected
    """
    userid = ndb.StringProperty()
    user_alias = ndb.StringProperty()
    token = ndb.StringProperty()
    last_ack = ndb.DateTimeProperty()


class ConversationModel(db.Model):
    """Model a single line of chat. All rows will keep the conversation
    """
    userid = ndb.StringProperty()
    user_alias = ndb.StringProperty()
    text = ndb.StringProperty()
    said = ndb.DateTimeProperty(auto_now=True)

