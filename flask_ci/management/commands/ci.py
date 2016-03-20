from importlib import import_module

import os
from flask.ext.script import Command, Option


class CICommand(Command):
    """
    Perform CI operations
    :param settings: settings
    """

    help = description = 'Perform CI operations.'

    def __init__(self, settings):
        super(Command, self).__init__()
        self.tasks_cls = [import_module(module_name).Reporter for module_name in self.get_task_list(settings)]
        self.tasks = [task_cls() for task_cls in self.tasks_cls]

    @staticmethod
    def get_task_list(settings):
        return getattr(settings, 'JENKINS_TASKS', ())

    def get_options(self):
        return [
            Option('-o', '--output-dir', dest='output_dir', default='reports'),
            Option('-v', '--verbose', action='store_true', dest='verbose', default=False)
        ]

    def __call__(self, *args, **kwargs):
        output_dir = kwargs['output_dir']
        verbose = kwargs['verbose']

        if not os.path.exists(output_dir):
            if verbose:
                print 'Creating output directory...'
            os.makedirs(output_dir)

        for task in self.tasks:
            if verbose:
                print('Executing {0}...'.format(task.__module__))
            task.run(**kwargs)

        if verbose:
            print('Done')
