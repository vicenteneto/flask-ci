from flask.ext.testing import TestCase
from flask_ci_test.app import create_app


class TestUsersViews(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app

    def test_create(self):
        response = self.client.post('/users')
        self.assertEquals(response.data, 'Create user')

    def test_list(self):
        response = self.client.get('/users')
        self.assertEquals(response.data, 'List users')

    def test_read(self):
        response = self.client.get('/users/1')
        self.assertEqual(response.data, 'Read user 1')

    def test_delete(self):
        response = self.client.delete('/users/1')
        self.assertEqual(response.data, 'Delete user 1')

    def test_update(self):
        response = self.client.put('/users/1')
        self.assertEqual(response.data, 'Update user 1')
