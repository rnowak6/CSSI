from google.appengine.ext import ndb
import webapp2
from user import User

class Post(ndb.Model):
    image = ndb.BlobProperty()
    desc = ndb.StringProperty()
    user = ndb.KeyProperty(User, repeated = True)
