# -*- coding: utf-8 -*-
"""
    flask_ci
    ~~~~~~~~~~~

    Continuous Integration support for Flask

    :copyright: (c) 2016 by Vicente Neto.
    :license: MIT, see LICENSE for more details.
"""
import os
from importlib import import_module

from flask_script import Command, Option


class CICommand(Command):
    """
    Perform CI operations
    :param settings: settings
    """

    help = description = 'Perform CI operations.'

    def __init__(self, settings):
        self.tasks_cls = [import_module(module_name).Reporter for module_name in self.get_task_list(settings)]
        self.tasks = [task_cls() for task_cls in self.tasks_cls]
        self.settings = settings

    @staticmethod
    def get_task_list(settings):
        return getattr(settings, 'CI_TASKS', ())

    def get_options(self):
        options = [
            Option('-o', '--output-dir', dest='output_dir', default='reports'),
            Option('-v', '--verbose', action='store_true', dest='verbose', default=False)
        ]

        for task in self.tasks:
            if hasattr(task, 'get_arguments'):
                options = options + task.get_arguments()

        return options

    def __call__(self, *args, **kwargs):
        output_dir = kwargs['output_dir']
        verbose = kwargs['verbose']

        if not os.path.exists(output_dir):
            if verbose:
                print('Creating output directory...')
            os.makedirs(output_dir)

        for task in self.tasks:
            if verbose:
                print('Executing {0}...'.format(task.__module__))
            task.run(self.settings, **kwargs)

        if verbose:
            print('Done')
