class Common:
    PARAM = '--'
    REPORTS = 'reports'


class CI:
    OUTPUT_DIR = 'output_dir'
    OUTPUT_DIR_PARAM = Common.PARAM + OUTPUT_DIR
    VERBOSE = 'verbose'
    VERBOSE_PARAM = Common.PARAM + VERBOSE


class FlaskScript:
    STORE_TRUE = 'store_true'


class Nose:
    COVER_BRANCHES = 'cover-branches'
    COVER_BRANCHES_PARAM = Common.PARAM + COVER_BRANCHES
    COVER_HTML = 'cover-html'
    COVER_HTML_PARAM = Common.PARAM + COVER_HTML
    COVER_HTML_DIR = 'cover-html-dir'
    COVER_HTML_DIR_PARAM = Common.PARAM + COVER_HTML_DIR
    COVER_PACKAGE = 'cover-package'
    COVER_PACKAGE_PARAM = Common.PARAM + COVER_PACKAGE
    COVER_XML = 'cover-xml'
    COVER_XML_PARAM = Common.PARAM + COVER_XML
    COVER_XML_FILE = 'cover-xml-file'
    COVER_XML_FILE_PARAM = Common.PARAM + COVER_XML_FILE
    COVERAGE_FILE = '.coverage'
    NOSE_TESTS = 'nosetests'
    WITH_COVERAGE = 'with-coverage'
    WITH_COVERAGE_PARAM = Common.PARAM + WITH_COVERAGE
    WITH_XUNIT = 'with-xunit'
    WITH_XUNIT_PARAM = Common.PARAM + WITH_XUNIT
    XUNIT_FILE = 'xunit-file'
    XUNIT_FILE_PARAM = Common.PARAM + XUNIT_FILE


class Pep8:
    CONFIG_FILE = 'config_file'
    PEP8_MAX_LINE_LENGTH = 'pep8-max-line-length'
    PEP8_MAX_LINE_LENGTH_PARAM = Common.PARAM + PEP8_MAX_LINE_LENGTH
    PEP8_RC_FILE = 'pep8-rcfile'
    PEP8_RC_FILE_PARAM = Common.PARAM + PEP8_RC_FILE
    MAX_LINE_LENGTH = 'max_line_length'


class PyLint:
    PYLINT_RC = 'pylint.rc'
    PYLINT_RC_FILE = 'pylint-rcfile'
    PYLINT_RC_FILE_PARAM = Common.PARAM + 'pylint-rcfile'
    RC_FILE = 'rcfile'
    RC_FILE_PARAM = Common.PARAM + RC_FILE


class Reports:
    COVERAGE = Common.REPORTS + '/coverage.xml'
    HTML_COVERAGE = Common.REPORTS + '/html-coverage'
    NOSE_TESTS = Common.REPORTS + '/nosetests.xml'
    PEP8_REPORT = 'pep8.report'
    PYLINT_REPORT = 'pylint.report'


class Settings:
    CI_TASKS = 'CI_TASKS'
    PEP8_RC_FILE = 'PEP8_RCFILE'
    PROJECT_APPS = 'PROJECT_APPS'
    PYLINT_RC_FILE = 'PYLINT_RCFILE'
