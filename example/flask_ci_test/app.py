from flask import Flask
from flask_ci_test_users import views as users_views


def create_app():
    flask_sample = Flask('flask_ci_test')

    flask_sample.register_blueprint(users_views.blueprint)

    return flask_sample
