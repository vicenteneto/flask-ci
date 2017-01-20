import os.path

import pep8
from flask_script import Option

from flask_ci.util.constants import CI, Pep8, Reports, Settings


class Reporter(object):
    @staticmethod
    def get_arguments():
        return [
            Option(Pep8.PEP8_RC_FILE_PARAM, dest=Pep8.PEP8_RC_FILE),
            Option(Pep8.PEP8_MAX_LINE_LENGTH_PARAM, dest=Pep8.PEP8_MAX_LINE_LENGTH, type=int, default=120)
        ]

    @staticmethod
    def get_config_path(settings, options):
        if options.get(Pep8.PEP8_RC_FILE, None):
            return options[Pep8.PEP8_RC_FILE]

        rcfile = getattr(settings, Settings.PEP8_RC_FILE, '')
        if os.path.exists(rcfile):
            return rcfile

    def run(self, settings, **options):
        output = open(os.path.join(options[CI.OUTPUT_DIR], Reports.PEP8_REPORT), 'w')

        class JenkinsReport(pep8.BaseReport):
            def error(self, line_number, offset, text, check):
                code = super(JenkinsReport, self).error(line_number, offset, text, check)
                if code:
                    source_line = self.line_offset + line_number
                    output.write('%s:%s:%s: %s\n' % (self.filename, source_line, offset + 1, text))

        pep8_options = {}
        config_file = self.get_config_path(settings, options)
        if config_file is not None:
            pep8_options[Pep8.CONFIG_FILE] = config_file

        pep8_options[Pep8.MAX_LINE_LENGTH] = options[Pep8.PEP8_MAX_LINE_LENGTH]

        pep8style = pep8.StyleGuide(
            parse_argv=False,
            reporter=JenkinsReport,
            **pep8_options)

        pep8style.options.report.start()
        for location in getattr(settings, Settings.PROJECT_APPS, []):
            pep8style.input_dir(os.path.relpath(location))
        pep8style.options.report.stop()

        output.close()
