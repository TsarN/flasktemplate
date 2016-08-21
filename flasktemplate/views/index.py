# -*- coding: utf-8 -*-

from flasktemplate import app

@app.route('/')
def index():
    return "Hello, world"
