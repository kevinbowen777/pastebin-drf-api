## pastebin-drf-api

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]()
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/pastebin-drf-api.svg)](https://github.com/kevinbowen777/pastebin-drf-api/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

- A simple pastebin code highlighting Web API

A browsable Web API built using Django REST Framework(DRF) that allows
authenticated users to post code snippets in the language of their choice
and have them highlighted using a number of code formatting styles.

##### Table of Contents
 - [Features](#features)
 - [Installation](#installation)
 - [Testing](#testing)
 - [API URLs](#api-urls)
 - [Application Demo](#application-demo)
 - [Screenshots](#screenshots)
 - [Reporting Bugs](#reporting-bugs)

---

### Features
 - Application
     - Browseable Web API
     - Schema API documentation
     - User registration with email verification & social(GitHub) login
     - Bootstrap4 & crispy-forms decorations
     - Customizable user profile pages with bio, profile pic, & country flags
 - Dev/testing
     - Basic module testing templates
     - Coverage reports
     - Debug-toolbar available
     - Examples of using Factories & pytest fixtures in account app testing
     - `shell_plus` with IPython via `django-extensions` package
     - Nox testing sessions for latest Python 3.9, 3.10, 3.11, and 3.12
         - black (`nox -s black`)
         - Sphinx documentation generation (`nox -s docs`)
         - linting (`nox -s lint`)
             - flake8
             - flake8-bugbear
             - flake8-docstrings
             - flake8-import-order
         - safety(python package vulnerability testing) (`nox -s safety`)
         - pytest sessions with coverage (`coverage run -m pytest`)
     - For additional links to package resources used in this repository, see the [Package Index](docs/package_index.md)

---

### Installation
 - `git clone https://github.com//kevinbowen777/pastebin-drf-api.git`
 - `cd pastebin-drf-api`
 - Local installation
     - `poetry install`
     - `python manage.py migrate`
     - `python manage.py createsuperuser`
     - `python manage.py runserver`
 - Docker installation
     - `docker compose up --build`
     - `docker compose exec web python manage.py migrate`
     - `docker compose exec web python manage.py createsuperuser`
     Additional commands:
       - `docker compose exec web python manage.py shell_plus`
         (loads Django shell autoloading project models & classes)
       - `docker run -it django-start-web bash`
         (CLI access to container)
 - Browse to http://127.0.0.1:8000 or http://127.0.0.1:8000/admin/

---

### Testing
 - `docker compose exec web python manage.py test`
 - `coverage run -m pytest`
 - Nox (includes sessions for black, lint, safety, tests)
     - testing supported for Python 3.9, 3.10, 3.11, 3.12
     - e.g. `nox`, `nox -rs lint-3.11`, `nox -s tests`

---

### API URLs

 - Log In endpoint:
    http://127.0.0.1:8000/api/v1/dj-rest-auth/login/
 - Log Out endpoint:
    http://127.0.0.1:8000/api/v1/dj-rest-auth/logout/
 - Password reset:
    http://127.0.0.1:8000/api/v1/dj-rest-auth/password/reset
 - Password reset confirmation:
    http://127.0.0.1:8000/api/v1/dj-rest-auth/password/reset/confirm
 - User registration endpoint:
    http://127.0.0.1:8000/api/v1/dj-rest-auth/registration/
 - User list:
    http://127.0.0.1:8000/api/v1/users/
 - User detail:
    http://127.0.0.1:8000/api/v1/users/1/
 - API schema download:
    http://127.0.0.1:8000/api/schema/

---

### Application Demo
A live application demonstration:

TBD

---

### Screenshots

### Home
![Home](https://github.com/kevinbowen777/pastebin-drf-api/blob/master/images/pastebin-drf-api_home.png)

### Index
![Message Index](https://github.com/kevinbowen777/pastebin-drf-api/blob/master/images/pastebin-drf-api_index.png)

### Profile Page
![Profile Page](https://github.com/kevinbowen777/pastebin-drf-api/blob/master/images/pastebin-drf-api_profile-page.png)

### Login Page
![Login Page](https://github.com/kevinbowen777/pastebin-drf-api/blob/master/images/pastebin-drf-api_sign-in.png)

### Snippet 
![Snippet](https://github.com/kevinbowen777/pastebin-drf-api/blob/master/images/pastebin-drf-api_snippet.png)
### Snippet List View
![Snippet List View](https://github.com/kevinbowen777/pastebin-drf-api/blob/master/images/pastebin-drf-api_snippet-list-view.png)

### Snippet List Detail
![Snippet List Detail](https://github.com/kevinbowen777/pastebin-drf-api/blob/master/images/pastebin-drf-api_snippet-list-detail.png)

### Swagger-UI
![Swagger-UI](https://github.com/kevinbowen777/pastebin-drf-api/blob/master/images/pastebin-drf-api_swagger-ui.png)

### Redoc API page
![Redoc API page](https://github.com/kevinbowen777/pastebin-drf-api/blob/master/images/pastebin-drf-api_redoc-tree.png)

### Email Address management
![Email Address management](https://github.com/kevinbowen777/pastebin-drf-api/blob/master/images/pastebin-drf-api_email-addresses.png)
---
### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/pastebin-drf-api/issues)
      to view currently open bug reports or open a new issue.
