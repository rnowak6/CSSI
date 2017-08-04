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
import json
import urllib2
import urllib
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        my_template=jinja_environment.get_template("templates/api.html")
        base_url = "http://api.giphy.com/v1/gifs/search?"
        url_params = {'q' : 'ryan gossling', 'api_key' : 'dc6zaTOxFJmzC', 'limit' : 10}
        request_url=base_url+urllib.urlencode(url_params)
        #giphy_data_source = urllib2.urlopen(
        #    "http://api.giphy.com/v1/gifs/search?q=puppies&api_key=dc6zaTOxFJmzC&limit=10")
        #self.response.write(giphy_data_source)
        giphy_response=urllib2.urlopen(request_url)
        giphy_json = giphy_response.read()
        giphy_data=json.loads(giphy_json)
        giphy_url=giphy_data['data'][0]['images']['original']['url']
        render_data={'image_url' : giphy_url}
        self.response.write(my_template.render(render_data))
        #parsed_giphy_dictionary = json.loads(giphy_json_content)
        #gif_url = parsed_giphy_dictionary['data'][0]['images']['original']['url']
        #render_data={'gif' : gif_url}
        #self.response.out.write("<img src = "+gif_url+">")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
