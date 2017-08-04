#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from snack import Snack

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class SnackHandler(webapp2.RequestHandler):
    def get(self):
        name=self.request.get("name")
        my_snack=Snack(kind = name)
        my_snack.put()

class DisplayHandler(webapp2.RequestHandler):
    def get(self):
        query=Snack.query()
        self.response.write("<ul>")
        for item in query.fetch():
            self.response.write("<li>")
            self.response.write(item.kind+ "</li>"+"<br>")
            self.response.write("</ul>")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/snack', SnackHandler),
    ('/display', DisplayHandler)
], debug=True)
