import os

from flask_script import Option

from flask_ci.util.constants import FlaskScript, Nose, Reports, Settings


class Reporter(object):
    @staticmethod
    def get_arguments():
        return [
            Option(Nose.WITH_XUNIT_PARAM, action=FlaskScript.STORE_TRUE, dest=Nose.WITH_XUNIT, default=False),
            Option(Nose.XUNIT_FILE_PARAM, dest=Nose.XUNIT_FILE, default=Reports.NOSE_TESTS),
            Option(Nose.COVER_XML_PARAM, action=FlaskScript.STORE_TRUE, dest=Nose.COVER_XML, default=False),
            Option(Nose.COVER_XML_FILE_PARAM, dest=Nose.COVER_XML_FILE, default=Reports.COVERAGE),
            Option(Nose.COVER_HTML_PARAM, action=FlaskScript.STORE_TRUE, dest=Nose.COVER_HTML, default=False),
            Option(Nose.COVER_HTML_DIR_PARAM, dest=Nose.COVER_HTML_DIR, default=Reports.HTML_COVERAGE),
            Option(Nose.COVER_BRANCHES_PARAM, action=FlaskScript.STORE_TRUE, dest=Nose.COVER_BRANCHES, default=False)
        ]

    def run(self, settings, **options):
        args = list()

        if options[Nose.WITH_XUNIT]:
            args.append(Nose.WITH_XUNIT_PARAM)
            args.append('%s=%s' % (Nose.XUNIT_FILE_PARAM, options[Nose.XUNIT_FILE]))
        if options[Nose.COVER_XML] or options[Nose.COVER_HTML]:
            args.append(Nose.WITH_COVERAGE_PARAM)
            args.append('%s=%s' % (Nose.COVER_PACKAGE_PARAM, ','.join(getattr(settings, Settings.PROJECT_APPS, []))))
        if options[Nose.COVER_XML]:
            args.append(Nose.COVER_XML_PARAM)
            args.append('%s=%s' % (Nose.COVER_XML_FILE_PARAM, options[Nose.COVER_XML_FILE]))
        if options[Nose.COVER_HTML]:
            args.append(Nose.COVER_HTML_PARAM)
            args.append('%s=%s' % (Nose.COVER_HTML_DIR_PARAM, options[Nose.COVER_HTML_DIR]))
        if options[Nose.COVER_BRANCHES]:
            args.append(Nose.COVER_BRANCHES_PARAM)

        command = '%s %s' % (Nose.NOSE_TESTS, ' '.join(args))
        os.system(command)

        if Nose.WITH_COVERAGE_PARAM in args:
            os.remove(Nose.COVERAGE_FILE)
