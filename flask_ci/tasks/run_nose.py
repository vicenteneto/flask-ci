from flask.ext.script import Option
import nose


class Reporter(object):
    @staticmethod
    def get_arguments():
        return [
            Option('-c', '--with-coverage', action='store_true', dest='with-coverage', default=False),
            Option('-x', '--with-xunit', action='store_true', dest='with-xunit', default=False)
        ]

    def run(self, settings, **options):
        args = list()

        if options.get('with-xunit', None):
            args.append('--with-xunit')
        if options.get('with-coverage', None):
            args.append('--with-coverage')
            args.append('--cover-xml')
            args.append('--cover-package=%s' % ','.join(getattr(settings, 'PROJECT_APPS', [])))

        args += getattr(settings, 'PROJECT_APPS', [])

        nose.run(argv=args)
