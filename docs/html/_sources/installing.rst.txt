Installation
============

Cloning the project
-------------------

To install the ``pastebin-drf-api`` project, run the following command in your terminal:

.. code-block:: console

   $ git clone https://github.com/kevinbowen777/pastebin-drf-api.git
   $ cd pastebin-drf-api

Local installation
^^^^^^^^^^^^^^^^^^

.. code-block:: console

   $ poetry shell
   $ poetry install
   $ python manage.py migrate
   $ python manage.py createsuperuser

Docker installation
^^^^^^^^^^^^^^^^^^^

.. code-block:: console

   $ docker compose up --build
   $ docker compose python manage.py migrate
   $ docker compose python manage.py createsuperuser

   Additional commands:
   $ docker compose exec web python manage.py shell_plus
     (loads Django shell autoloading the project models & classes)
   $ docker run -it pastebin-drf-api-web bash
     (CLI access to container)

Pre-commit installation
^^^^^^^^^^^^^^^^^^^^^^^
To add the pre-commit hooks, run the following command in the poetry shell:

.. code-block:: console

   $ pre-commit install

Usage
-----

To run pastebin-drf-api, locally, enter the following on the command line:

.. code-block:: console

   $ python manage.py runserver

For both local, or Docker installations, browse to `<http://127.0.0.1:8000>`_ or `<http://127.0.0.1:8000/resources/>`_ for access to the admin panel.

API URLs
--------
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
