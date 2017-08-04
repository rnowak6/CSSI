from google.appengine.ext import ndb
from random import randint
import urllib2

response = urllib2.urlopen("https://uinames.com/api/")

class RedditPost(ndb.Model):
    title = ndb.StringProperty()
    desc = ndb.StringProperty()
    score = ndb.IntegerProperty()
    username = ndb.StringProperty()
    likes = ndb.IntegerProperty()
