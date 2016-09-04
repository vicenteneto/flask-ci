#!/usr/bin/env python
from flask_ci import CICommand
from flask_ci_test import app, settings
from flask_script import Manager

manager = Manager(app.create_app())
manager.add_command('ci', CICommand(settings))

if __name__ == '__main__':
    manager.run()
