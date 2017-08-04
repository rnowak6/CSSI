from google.appengine.ext import ndb
import webapp2


class Snack(ndb.Model):
    kind=ndb.StringProperty()
    rating=ndb.IntegerProperty(repeated = True)
    quantity=ndb.IntegerProperty()
    calories=ndb.IntegerProperty()
    expiration=ndb.DateTimeProperty()
