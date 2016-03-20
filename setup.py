"""
Flask-CI
--------

Provide Continuous Integration support operations for Flask apps.
"""
from setuptools import setup

version = '0.3.19'
install_requires = ['Flask-Script', 'Pep8', 'Pylint']

setup(
    name='Flask-CI',
    version=version,
    description='Continuous Integration support for Flask',
    url='https://github.com/vicenteneto/flask-ci',
    author='Vicente Neto',
    author_email='sneto.vicente@gmail.com',
    license='MIT',
    packages=['flask_ci', 'flask_ci.management', 'flask_ci.tasks', 'flask_ci.management.commands'],
    install_requires=install_requires,
    package_data={'flask_ci': ['tasks/pylint.rc', 'tasks/pep8.rc']},
    zip_safe=False
)
