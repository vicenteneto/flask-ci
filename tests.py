from flask.ext.script import Manager


class TestManager:
    def __init__(self):
        self.app = None

    def test_with_default_commands(self):
        manager = Manager(self.app)
        manager.set_defaults()

        assert 'runserver' in manager._commands
        assert 'shell' in manager._commands
