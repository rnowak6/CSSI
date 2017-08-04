from google.appengine.ext import ndb
import webapp2

class User(ndb.Model):
    username = ndb.StringProperty()
    bio = ndb. StringProperty()
