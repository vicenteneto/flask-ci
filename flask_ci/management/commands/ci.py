from flask.ext.script import Command


class CICommand(Command):
    """
    Perform CI operations
    :param settings: settings
    """

    help = description = 'Perform CI operations.'

    def __init__(self, settings):
        super(Command, self).__init__()
