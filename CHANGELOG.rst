.. _`changelog`:

=========
Changelog
=========

``pastebin-drf-api`` issues are filed on `GitHub <https://github.com/kevinbowen777/pastebin-drf-api/issues>`_, and each ticket number here corresponds to a closed GitHub issue.

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_, and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

This project uses `towncrier <https://towncrier.readthedocs.io/>`_ for keeping
the changelog. DO NOT commit any changes to this file.

Backward incompatible (breaking) changes should only be introduced in major versions
with advance notice in the **Deprecations** section of releases.


..
    You should *NOT* be adding new change log entries to this file, this
    file is managed by towncrier. You *may* edit previous change logs to
    fix problems like typo corrections or such.
    To add a new change log entry, please see
    https://pip.pypa.io/en/latest/development/contributing/#news-entries
    but note that in toolbox the "news/" directory is named "changelog/".

.. towncrier release notes start

pastebin-drf-api 0.3.5 (2026-08-24)
===================================

Improved documentation
----------------------

-  (`#572 <https://github.com/kevinbowen777/pastebin-drf-api/572>`_): Add towncrier 25.8.0.


New features
------------

-  (`#596 <https://github.com/kevinbowen777/pastebin-drf-api/596>`_): Upgrade to Django 6.0.8

pastebin-drf-api 0.3.4 (2026-07-31)
===================================

Contributor-facing changes
--------------------------

- : Add Python 3.14 support.

-  (`#587 <https://github.com/kevinbowen777/pastebin-drf-api/587>`_): Rename default branch to main.

-  (`#590 <https://github.com/kevinbowen777/pastebin-drf-api/590>`_): Update with Python 3.14.6 & 3.13.14.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#573 <https://github.com/kevinbowen777/pastebin-drf-api/573>`_): Drop support for Python 3.11.


New features
------------

-  (`#556 <https://github.com/kevinbowen777/pastebin-drf-api/556>`_): Upgrade Django to 6.0.7.

pastebin-drf-api 0.3.3 (2025-05-08)
===================================

Contributor-facing changes
--------------------------

-  (`#492 <https://github.com/kevinbowen777/pastebin-drf-api/492>`_): Upgrade PostgreSQL to 15.11.

-  (`#503 <https://github.com/kevinbowen777/pastebin-drf-api/503>`_): Update Poetry to 2.1.2.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#498 <https://github.com/kevinbowen777/pastebin-drf-api/498>`_): Drop Python 3.10 support.


Improved documentation
----------------------

-  (`#497 <https://github.com/kevinbowen777/pastebin-drf-api/497>`_): Update Sphinx to 8.2.3.


New features
------------

-  (`#485 <https://github.com/kevinbowen777/pastebin-drf-api/485>`_): Upgrade Docker image to Python 3.13

-  (`#502 <https://github.com/kevinbowen777/pastebin-drf-api/502>`_): Upgrade Django Rest Framework to 3.16.0.

-  (`#504 <https://github.com/kevinbowen777/pastebin-drf-api/504>`_): Upgrade Django to 5.2.


Security updated
----------------

-  (`#507 <https://github.com/kevinbowen777/pastebin-drf-api/507>`_): Replace safety package with pip-audit.

pastebin-drf-api 0.3.2 (2025-01-24)
===================================

Contributor-facing changes
--------------------------

-  (`#435 <https://github.com/kevinbowen777/pastebin-drf-api/435>`_): Add support for Python 3.13

-  (`#480 <https://github.com/kevinbowen777/pastebin-drf-api/480>`_): Re-build pyproject for Poetry 2.0.


New features
------------

-  (`#471 <https://github.com/kevinbowen777/pastebin-drf-api/471>`_): Upgrade Django to 5.1.4

pastebin-drf-api 0.3.0 (2023-12-27)
===================================

Contributor-facing changes
--------------------------

-  (`#182 <https://github.com/kevinbowen777/pastebin-drf-api/182>`_): Migrate to non-root Docker user & venv.

-  (`#186 <https://github.com/kevinbowen777/pastebin-drf-api/186>`_): Update Python to 3.12.0.

-  (`#337 <https://github.com/kevinbowen777/pastebin-drf-api/337>`_): Upgrade Poetry to 1.7.1.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#334 <https://github.com/kevinbowen777/pastebin-drf-api/334>`_): Drop support for Python 3.9.


Improved documentation
----------------------

- : Update Sphinx theme to Furo


New features
------------

-  (`#345 <https://github.com/kevinbowen777/pastebin-drf-api/345>`_): Upgrade to Django 5.0.

pastebin-drf-api 0.2.0 (2023-05-21)
===================================

Contributor-facing changes
--------------------------

-  (`#218 <https://github.com/kevinbowen777/pastebin-drf-api/218>`_): Install ruff. Drop flake8-* packages.

pastebin-drf-api 0.1.0 (2023-05-08)
===================================

Contributor-facing changes
--------------------------

- : Add django-debug-toolbar.

- : Mirror to GitLab.

-  (`#179 <https://github.com/kevinbowen777/pastebin-drf-api/179>`_): Migrate from SQLite to PostgreSQL

-  (`#191 <https://github.com/kevinbowen777/pastebin-drf-api/191>`_): Add support for Python 3.12.

-  (`#198 <https://github.com/kevinbowen777/pastebin-drf-api/198>`_): Re-write for compatibility with Poetry 1.4.1.

-  (`#202 <https://github.com/kevinbowen777/pastebin-drf-api/202>`_): Upgrade PostgreSQL to 15.2

-  (`#220 <https://github.com/kevinbowen777/pastebin-drf-api/220>`_): Upgrade Django to 4.2.1

-  (`#3 <https://github.com/kevinbowen777/pastebin-drf-api/3>`_): Implement nox for testing


Improved documentation
----------------------

- : Add Sphinx for documentation


New features
------------

-  (`#30 <https://github.com/kevinbowen777/pastebin-drf-api/30>`_): Build Docker support for Heroku deployment.

pastebin-drf-api 0.0.1 (2022-03-31)
===================================

Contributor-facing changes
--------------------------

- : Add support for Python 3.10


New features
------------

- : Support Django 4.0.6


Miscellaneous internal changes
------------------------------

- : Initial commit
