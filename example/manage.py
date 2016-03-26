#!/usr/bin/env python
from flask.ext.ci import CICommand
from flask.ext.script import Manager
from flask_ci_test import app, settings

manager = Manager(app.create_app())
manager.add_command('ci', CICommand(settings))

if __name__ == '__main__':
    manager.run()
