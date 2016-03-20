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

.. image:: http://img.shields.io/:license-mit-blue.svg
    :target: https://github.com/vicenteneto/flask-ci/blob/master/LICENSE
    :alt: License

Continuous Integration with Flask

Table of contents
-----------------

* `Installation <#installation>`_
* `Usage <#usage>`_
* `Settings <#settings>`_
* `Reporters <#reporters>`_
* `Contributing <#contributing>`_
* `Creator <#creator>`_
* `Copyright and License <#copyright-and-license>`_

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

Import the CICommand sub-manager::

    from flask_ci.management.commands.ci import CICommand

Register the CICommand sub-manager to your primary Manager (within manage.py)::

    manager = Manager(create_app())
    manager.add_command('ci', CICommand(settings))

Configure your continuous integration tool to run the following command::

    $ python manage.py ci

Settings
--------

- ``PROJECT_APPS``
    A list/tuple of the custom apps you’ve written for your project. Reports are generated only for the apps from this list.

- ``CI_TASKS``
    List of Continuous Integration reporters executed by ``python manage.py ci`` command.
        Default value: ``CI_TASKS = []``

Reporters
--------
Here is the reporters prebuild with Flask-CI.

- ``flask_ci.tasks.run_pylint``
    Runs `Pylint <http://www.logilab.org/project/pylint>`_ over selected apps.
    Task-specific settings: ``PYLINT_RCFILE``

- ``flask_ci.tasks.run_pep8``
    Runs pep8 tool over selected apps.
    Task-specific settings: ``PEP8_RCFILE``

Contributing
------------

Have a bug or a feature request? `Please, open a GitHub issue <https://github.com/vicenteneto/flask-ci/issues/new>`_.

Creator
-------

**Vicente Neto**

* <https://github.com/vicenteneto>

Copyright and license
---------------------

Copyright 2016-, Vicente Neto. This project is licensed under the `MIT License <https://github.com/vicenteneto/flask-ci/blob/master/LICENSE>`_.
