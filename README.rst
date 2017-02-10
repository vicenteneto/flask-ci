Flask-CI
========
.. image:: https://img.shields.io/pypi/v/flask-ci.svg
    :target: https://pypi.python.org/pypi/flask-ci

.. image:: https://img.shields.io/pypi/dm/flask-ci.svg
    :target: https://pypi.python.org/pypi/flask-ci

.. image:: https://travis-ci.org/vicenteneto/flask-ci.svg?branch=master
    :target: https://travis-ci.org/vicenteneto/flask-ci
    :alt: Build Status

.. image:: https://requires.io/github/vicenteneto/flask-ci/requirements.svg?branch=master
    :target: https://requires.io/github/vicenteneto/flask-ci/requirements/?branch=master
    :alt: Requirements Status

.. image:: http://img.shields.io/:status-beta-yellowgren.svg
    :target: https://pypi.python.org/pypi/flask-ci
    :alt: Status

.. image:: http://img.shields.io/:license-mit-blue.svg
    :target: https://github.com/vicenteneto/flask-ci/blob/master/LICENSE
    :alt: License

Continuous Integration with Flask.

Table of contents
-----------------
* `Installation <#installation>`_
* `Usage <#usage>`_
* `Settings <#settings>`_
* `Reporters <#reporters>`_
* `Changes <#changes>`_
* `Contributing <#contributing>`_
* `Creator <#creator>`_
* `Copyright and License <#copyright-and-license>`_
* `Changes <#changes>`_
* `3rd Party Stuff <#3rd-party-stuff>`_

Installation
------------
From PyPI::

    $ pip install Flask-CI

Or by downloading the source and running::

    $ python setup.py install

Latest git version::

    $ pip install git+https://github.com/vicenteneto/flask-ci.git#egg=Flask-CI

Usage
-----
Consider you have this code::

    # manage.py

    from flask_script import Manager

    from myapp import app, settings

    manager = Manager(app.create_app(settings))

    if __name__ == "__main__":
        manager.run()

Import the CICommand sub-manager::

    from flask_ci import CICommand

Register the CICommand sub-manager to your primary Manager (within manage.py)::

    manager.add_command('ci', CICommand(settings))

Configure your continuous integration tool to run the following command::

    $ python manage.py ci

Settings
--------
- ``CI_TASKS``
    List of Continuous Integration reporters executed by ``python manage.py ci`` command.

- ``PROJECT_APPS``
    A list of the custom apps you’ve written for your project. Reports are generated only for the apps from this list.

Sample::

    # settings.py

    CI_TASKS = (
        'flask_ci.tasks.run_nose',
        'flask_ci.tasks.run_pep8',
        'flask_ci.tasks.run_pylint'
    )

    PROJECT_APPS = (
        'flask_ci_test',
        'flask_ci_test_users'
    )

Reporters
---------
Here is the reporters prebuild with Flask-CI.

- ``flask_ci.tasks.run_nose``
    Runs `Nose <https://nose.readthedocs.org/en/latest>`_ over selected apps.

- ``flask_ci.tasks.run_pep8``
    Runs `Pep8 <http://pep8.readthedocs.org/en/latest/index.html>`_ tool over selected apps. Task-specific settings: ``PEP8_RCFILE``.

- ``flask_ci.tasks.run_pylint``
    Runs `Pylint <http://www.logilab.org/project/pylint>`_ over selected apps. Task-specific settings: ``PYLINT_RCFILE``.
https://github.com/vicenteneto

Contributing
------------
Have a bug or a feature request? `Please, open a GitHub issue <https://github.com/vicenteneto/flask-ci/issues/new>`_.

**Vicente Neto (creator)** - <https://github.com/vicenteneto>

**Clement** - <https://github.com/clement10601>

Copyright and license
---------------------
Copyright 2016-, Vicente Neto. This project is licensed under the `MIT License <https://github.com/vicenteneto/flask-ci/blob/master/LICENSE>`_.


Changes
=======
1.2.9.1 - 2017-01-21
--------------------
- Unit tests
- Integration tests

1.1.20 - 2017-01-01
-------------------
- Code refactoring
- Updating requirements dependencies

0.12.21 - 2016-12-21
--------------------
- Python3 compatible

0.9.4 - 2016-09-04
------------------
- Updating requirements dependencies

0.3.25 - 2016-03-25
-------------------
- Fixing README usage error
- Added a test application

0.3.26 -- 2016-03-26
--------------------
- Refactoring project architecture
- Updating outdated requirements

0.4.15 -- 2016-04-15
--------------------
- Added Flask-Pylint plugin on pylint reports

0.4.22 -- 2016-04-22
--------------------
- Fixing nose tests task execution


3rd Party Stuff
===============
Flask-CI is built with the help of `Flask-Script <https://flask-script.readthedocs.org/en/latest/>`_.
