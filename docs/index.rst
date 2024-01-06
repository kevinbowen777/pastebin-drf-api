pastebin-drf-api
================

.. toctree::
   :hidden:
   :maxdepth: 1

   license
   package_index
   create_new_users
   add_code_list

.. contents:: Table of Contents
   :local:
   :backlinks: top
   :depth: 2

A simple pastebin code highlighting Web API built with the Django 5.0.x web framework and the Django REST Framework(DRF).

A browsable Web API built using Django REST Framework(DRF) that allows
authenticated users to post code snippets in the language of their choice
and have them highlighted using a number of code formatting styles.

Features
--------

 * Application

   * Browseable Web API
   * SwaggerUI & ReDoc API documentation
   * User registration with email verification & social(GitHub) login using `django-allauth <https://pypi.org/project/django-allauth/>`_
   * `Bootstrap4 <https://pypi.org/project/django-bootstrap4/>`_ & `crispy-forms <https://pypi.org/project/django-crispy-forms/>`_ decorations
   * Customizable user profile pages with bio, profile pic, & `country flags <https://pypi.python.org/pypi/django-countries>`_
   * For links to additional package resources used in this repository, see the :doc:`Package Index <package_index>`
 * Dev/testing

   * Basic module testing templates
   * `Coverage <https://pypi.org/project/coverage/>`_ reports in `htmlcov` directory
   * `Debug-toolbar <https://pypi.org/project/django-debug-toolbar/>`_ available. See notes in `config/settings.py` for enabling.
   * Examples of using `Factories <https://pypi.org/project/factory-boy/>`_ & `pytest <https://pypi.org/project/pytest/>`_ fixtures in account app testing
   * `shell_plus <https://django-extensions.readthedocs.io/en/latest/shell_plus.html>`_ with `IPython <https://pypi.org/project/ipython/>`_ via `django-extensions <https://pypi.python.org/pypi/django-extensions/>`_ package
   * `Nox <https://pypi.org/project/nox/>`_ testing sessions for latest Python 3.9, 3.10, and 3.11, 3.12

     * `black <https://pypi.org/project/black/>`_
     * `Sphinx <https://pypi.org/project/Sphinx/>`_ documentaion generation
     * linting

       * `flake8 <https://pypi.org/project/flake8/>`_
       * `flake8-bandit <https://pypi.org/project/flake8-bandit/>`_
       * `flake8-bugbear <https://pypi.org/project/flake8-bugbear/>`_
       * `flake8-import-order <https://pypi.org/project/flake8-import-order/>`_
     * `safety <https://pypi.org/project/safety/)(python package vulnerability testing>`_
     * `pytest sessions <https://docs.pytest.org/en/latest/>`_ with `pytest-cov <https://pypi.org/project/pytest-cov/>`_ & `pytest-django <https://pypi.org/project/pytest-django/>`_
 * `run` command menu

(adapted from Nick Janetakis' helpful `docker-django-example <https://github.com/nickjj/docker-django-example/>`_)

You can run `./run` to get a list of commands and each command has documentation in the run file itself. This comes in handy to run various Docker commands because sometimes these commands can be a bit long to type.

*If you get tired of typing `./run` you can always create a shell alias with `alias run=./run` in your `~/.bash_aliases` or equivalent file. Then you'll be
able to run `run` instead of `./run`.*

Installation
------------

To install the pastebin-drf-api project,
run this command in your terminal:

.. code-block:: console

   $ git clone https://github.com/kevinbowen777/pastebin-drf-api.git
   $ cd pastebin-drf-api

Local installation
------------------

.. code-block:: console

   $ poetry shell
   $ poetry install
   $ python manage.py migrate
   $ python manage.py createsuperuser


Docker installation
-------------------

.. code-block:: console

   $ docker compose up --build
   $ docker compose python manage.py migrate
   $ docker compose python manage.py createsuperuser
   Additional commands:
   $ docker compose exec web python manage.py shell_plus
     (loads Django shell autoloading project models & classes)
   $ docker run -it django-start-web bash`
     (CLI access to container)

Usage
-----

To run pastebin-drf-api, locally, enter the following on the command line:

.. code-block:: console

   $ python manage.py runserver

For both local, or Docker installations, browse to `<http://127.0.0.1:8000>`_ or `<http://127.0.0.1:8000/resources/>`_

API URLs
----------------
 * Log In endpoint:
    `<http://127.0.0.1:8000/api/v1/dj-rest-auth/login/>`_
 * Log Out endpoint:
    `<http://127.0.0.1:8000/api/v1/dj-rest-auth/logout/>`_
 * Password reset:
    `<http://127.0.0.1:8000/api/v1/dj-rest-auth/password/reset>`_
 * Password reset confirmation:
    `<http://127.0.0.1:8000/api/v1/dj-rest-auth/password/reset/confirm>`_
 * User registration endpoint:
    `<http://127.0.0.1:8000/api/v1/dj-rest-auth/registration/>`_
 * User list:
    `<http://127.0.0.1:8000/api/v1/users/>`_
 * User detail:
    `<http://127.0.0.1:8000/api/v1/users/1/>`_
 * API schema download:
    `<http://127.0.0.1:8000/api/schema/>`_
 * Redoc API browser:
    `<http://127.0.0.1:8000/api/schema/redoc/>`_
 * Swagger-UI:
    `<http://127.0.0.1:8000/api/schema/swagger-ui/>`_

Testing
-------

.. code-block:: console

   $ python manage.py runserver
   $ docker compose exec web python manage.py test
   $ coverage run -m pytest
   $ nox --list-sessions
   $ nox
   $ nox -s black-3.12
   $ nox -s docs-3.11
   $ nox -rs lint-3.10  (Use the 'r' flag to reuse existing session)
   $ nox -s pyright-3.11
   $ nox -s safety  (will run tests against all Python versions)
   $ nox -s tests

Application Demo
----------------
Live demonstration of application:

TBD

Reporting Bugs
--------------

Visit the pastebin-drf-api `Issues page <https://github.com/kevinbowen777/pastebin-drf-api/issues>`_ on GitHub.
