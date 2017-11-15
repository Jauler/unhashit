#!/usr/bin/python

import webapp2
from main import app
from paste import httpserver

httpserver.serve(app, host="127.0.0.1", port="8080")




