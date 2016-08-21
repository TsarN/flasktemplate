# -*- coding: utf-8 -*-

import os.path

from flask_migrate import Migrate, MigrateCommand
from flasktemplate.console.manager import manager
from flasktemplate import app, db

migrate = Migrate(app, db)
if 'WORKDIR' in app.config:
    app.extensions['migrate'].directory = os.path.join(app.config.get('WORKDIR'), "migrations")
    app.extensions['migrate'].migrate.directory = app.extensions['migrate'].directory
manager.add_command('db', MigrateCommand)
