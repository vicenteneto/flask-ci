"""
Flask-CI
--------

Provide Continuous Integration support operations for Flask apps.

Links
`````

* `documentation <https://pythonhosted.org/Flask-CI>`_
* `development version <http://github.com/vicenteneto/flask-ci/zipball/master#egg=Flask-CI-dev>`_
"""
from setuptools import setup

version = '0.12.21'
packages = ['flask_ci', 'flask_ci.tasks']
install_requires = ['Coverage', 'Flask-Script', 'Nose', 'Pep8', 'Pylint', 'Pylint-Flask']
flask_ci_pkg_data = ['tasks/pylint.rc']

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
    keywords=['ci', 'jenkins', 'hudson', 'flask', 'pylint', 'pep8', 'coverage', 'nose'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing'
    ]
)
