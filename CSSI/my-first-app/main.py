#!/usr/bin/env python
# -*- coding: utf-8 -*-﻿
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
import jinja2
import webapp2
import os
from random import randint

#set up environment for Jinja
#this sets jinja's relative directory to match the directory name(dirname) of
#the current __file__, in this case, main.py
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):
    def random_greets(self):
        langs=["Hola", "Hi", "Cześć"]
        return langs[randint(0,2)]

    def build_response(self):
        return "sup peeps"


    def get(self):

        lang=self.random_greets()
        self.response.write(lang)

class MilkHandler(webapp2.RequestHandler):
    def get(self):
        mult=self.request.get("mult")
        mult=int(mult)
        self.response.write(2 * mult)

class ImageHandler(webapp2.RequestHandler):
    def get(self):
        my_template=jinja_environment.get_template("templates/hello-world.html")
        numb=self.request.get("times")
        if(numb==''):
            numb=1
        else:
            numb = int(numb)

        #vegetables=self.request.get("vegetables")
        render_data={'times' : numb}
        self.response.write(my_template.render(render_data))




        #hellos=["Hola", "Hi", "Czesc"]
        #hello=hellos[randint(0,len(hellos)-1)]
        #name=''
        #name=self.request.get("name")
        #if(name == ''):
        #    name='person'
        #my_template=jinja_environment.get_template("templates/hello-world.html")
        #self.response.write("something")
        #color=self.request.get("color")
        #render_data={'greeting' : hello,
        #    'name' : name,
        #    'color' : color }
        #self.response.write(my_template.render(render_data))
        #self.response.write("<head>")
        #self.response.write("<link rel='stylesheet' href='/resources/color.css' > ")
        #self.response.write("</head>")
        #self.response.write("<h1>My Handler Worked!</h1>")
        #self.response.write("<img src=/resources/milk.jpg>")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/milk', MilkHandler),
    ('/image', ImageHandler)
], debug=True)
