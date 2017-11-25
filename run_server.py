#!/usr/bin/python

import webapp2
from main import app
from paste.urlparser import StaticURLParser
from paste.cascade import Cascade
from paste import httpserver

static_app = StaticURLParser("html/")
my_app = Cascade([static_app, app])

httpserver.serve(my_app, host="0.0.0.0", port="8080")




