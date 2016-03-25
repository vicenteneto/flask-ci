import nose
import os
from flask.ext.script import Option


class Reporter(object):
    @staticmethod
    def get_arguments():
        return [
            Option('--with-xunit', action='store_true', dest='with-xunit', default=False),
            Option('--with-coverage', action='store_true', dest='with-coverage', default=False),
            Option('-x', '--cover-xml', action='store_true', dest='cover-xml', default=True),
            Option('-X', '--no-cover-xml', action='store_true', dest='no-cover-xml', default=False)
        ]

    def run(self, settings, **options):
        args = list()
        args.append('fake')

        if options['with-xunit']:
            args.append('--with-xunit')
        if options['with-coverage']:
            args.append('--with-coverage')
            args.append('--cover-package=%s' % ','.join(getattr(settings, 'PROJECT_APPS', [])))
        if options['cover-xml'] and not options['no-cover-xml']:
            args.append('--cover-xml')

        nose.run(argv=args)

        if options['with-xunit'] and os.path.isfile('nosetests.xml'):
            os.rename('nosetests.xml', 'reports/nosetests.xml')
        if options['with-coverage']:
            os.remove('.coverage')
        if options['with-coverage'] and options['cover-xml'] and not options['no-cover-xml']:
            os.rename('coverage.xml', 'reports/coverage.xml')
