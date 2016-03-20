"""
Flask-CI
--------

Provide Continuous Integration support operations for Flask apps.
"""
from setuptools import setup

version = '0.3.20'
packages = ['flask_ci', 'flask_ci.management', 'flask_ci.tasks', 'flask_ci.management.commands']
install_requires = ['Flask-Script', 'Pep8', 'Pylint']
flask_ci_pkg_data = ['tasks/pylint.rc', 'tasks/pep8.rc']

setup(
    name='Flask-CI',
    version=version,
    description='Continuous Integration support for Flask',
    url='https://github.com/vicenteneto/flask-ci',
    author='Vicente Neto',
    author_email='sneto.vicente@gmail.com',
    license='MIT',
    packages=packages,
    install_requires=install_requires,
    package_data={'flask_ci': flask_ci_pkg_data},
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing'
    ]
)
