import os
from flask.ext.script import Option
from pylint import lint
from pylint.reporters.text import TextReporter


class ParseableTextReporter(TextReporter):
    """
    Outputs messages in a form recognized by jenkins
    <filename>:<linenum>:<msg>
    """
    name = 'parseable'
    line_format = '{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}'


class Reporter(object):
    @staticmethod
    def get_arguments():
        return [
            Option('--pylint-rcfile', dest='pylint_rcfile')
        ]

    @staticmethod
    def get_config_path(settings, options):
        if options['pylint_rcfile']:
            return options['pylint_rcfile']

        rcfile = getattr(settings, 'PYLINT_RCFILE', 'pylint.rc')
        if os.path.exists(rcfile):
            return rcfile

        # use built-in
        root_dir = os.path.normpath(os.path.dirname(__file__))
        return os.path.join(root_dir, 'pylint.rc')

    def run(self, settings, **options):
        output = open(os.path.join(options['output_dir'], 'pylint.report'), 'w')

        args = list()
        args.append("--rcfile=%s" % self.get_config_path(settings, options))
        args += getattr(settings, 'PROJECT_APPS', [])

        lint.Run(args, reporter=ParseableTextReporter(output=output), exit=False)

        output.close()
