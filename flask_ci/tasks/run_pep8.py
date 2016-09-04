import os.path

import pep8
from flask_script import Option


class Reporter(object):
    @staticmethod
    def get_arguments():
        return [
            Option('--pep8-rcfile', dest='pep8-rcfile'),
            Option('--pep8-max-line-length', dest='pep8-max-line-length', type=int, default=120)
        ]

    @staticmethod
    def get_config_path(settings, options):
        if options.get('pep8-rcfile', None):
            return options['pep8-rcfile']

        rcfile = getattr(settings, 'PEP8_RCFILE', '')
        if os.path.exists(rcfile):
            return rcfile

    def run(self, settings, **options):
        output = open(os.path.join(options['output_dir'], 'pep8.report'), 'w')

        class JenkinsReport(pep8.BaseReport):
            def error(self, line_number, offset, text, check):
                code = super(JenkinsReport, self).error(line_number, offset, text, check)
                if code:
                    source_line = self.line_offset + line_number
                    output.write('%s:%s:%s: %s\n' % (self.filename, source_line, offset + 1, text))

        pep8_options = {}
        config_file = self.get_config_path(settings, options)
        if config_file is not None:
            pep8_options['config_file'] = config_file

        pep8_options['max_line_length'] = options['pep8-max-line-length']

        pep8style = pep8.StyleGuide(
            parse_argv=False,
            reporter=JenkinsReport,
            **pep8_options)

        pep8style.options.report.start()
        for location in getattr(settings, 'PROJECT_APPS', []):
            pep8style.input_dir(os.path.relpath(location))
        pep8style.options.report.stop()

        output.close()
