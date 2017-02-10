import os

from flask_script import Option
from pylint import lint
from pylint.reporters.text import TextReporter

from flask_ci.util.constants import CI, PyLint, Reports, Settings


class ParseableTextReporter(TextReporter):
    name = 'parseable'
    line_format = '{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}'


class Reporter(object):
    @staticmethod
    def get_arguments():
        return [
            Option(PyLint.PYLINT_RC_FILE_PARAM, dest=PyLint.PYLINT_RC_FILE)
        ]

    @staticmethod
    def get_config_path(settings, options):
        if options.get('pylint_rcfile', None):
            return options[PyLint.PYLINT_RC_FILE]

        rcfile = getattr(settings, Settings.PYLINT_RC_FILE, PyLint.PYLINT_RC)
        if os.path.exists(rcfile):
            return rcfile

        # use built-in
        root_dir = os.path.normpath(os.path.dirname(__file__))
        return os.path.join(root_dir, PyLint.PYLINT_RC)

    def run(self, settings, **options):
        output = open(os.path.join(options[CI.OUTPUT_DIR], Reports.PYLINT_REPORT), 'w')

        args = list()
        args.append('%s=%s' % (PyLint.RC_FILE_PARAM, self.get_config_path(settings, options)))
        args += getattr(settings, Settings.PROJECT_APPS, [])

        lint.Run(args, reporter=ParseableTextReporter(output=output), exit=False)

        output.close()
