# -*- coding: utf-8 -*-

APPNAME = "flasktemplate"

from flask import Flask
import flasktemplate.config
from flask_sqlalchemy import SQLAlchemy

class FlasktemplateApplication(Flask):
    "flasktemplate WSGI application"

    def __str__(self):
        return "<FlasktemplateApplication>"

app = FlasktemplateApplication("flasktemplate")
app.config.from_object(flasktemplate.config)
db = SQLAlchemy(app)

import flasktemplate.views
import flasktemplate.models
