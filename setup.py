"""
Flask-CI
--------

Provide Continuous Integration support operations for Flask apps.
"""
from setuptools import setup

version = '0.3.19'
install_requires = ['Flask-Script']

setup(
    name='Flask-CI',
    version=version,
    description='Continuous Integration support for Flask',
    url='https://github.com/vicenteneto/flask-ci',
    author='Vicente Neto',
    author_email='sneto.vicente@gmail.com',
    license='MIT',
    packages=['flask_ci'],
    install_requires=install_requires,
    zip_safe=False
)
