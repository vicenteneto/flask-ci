from flask.ext.script import Option
import nose


class Reporter(object):
    @staticmethod
    def get_arguments():
        return [
            Option('-c', '--with-coverage', action='store_true', dest='with-coverage', default=False),
            Option('-x', '--with-xunit', action='store_true', dest='with-xunit', default=False),
            Option('--cover-html', action='store_true', dest='cover-html', default=False),
            Option('--cover-xml', action='store_true', dest='cover-xml', default=False)
        ]

    def run(self, settings, **options):
        args = list()

        if options.get('with-coverage', None):
            args.append('--with-coverage')
        if options.get('with-xunit', None):
            args.append('--with-xunit')
        if options.get('cover-html'):
            args.append('--cover-html')
        if options.get('cover-xml'):
            args.append('--cover-xml')

        args.append('--cover-package=%s' % ','.join(getattr(settings, 'PROJECT_APPS', [])))

        args += getattr(settings, 'PROJECT_APPS', [])

        nose.run(argv=args)
