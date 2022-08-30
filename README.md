## pastebin-drf-api 

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/pastebin-drf-api.svg)](https://github.com/kevinbowen777/pastebin-drf-api/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

- A simple pastebin code highlighting Web API

A browsable Web API built using Django REST Framework(DRF) that allows
authenticated users to post code snippets in the language of their choice
and have them highlighted using a number of formatting styles.

### Installation
 - `git clone https://github.com//kevinbowen777/pastebin-drf-api.git`
 - `cd pastebin-drf-api`
 - `docker-compose up --build`
 - `docker-compose exec web python manage.py migrate`
 - `docker-compose exec web python manage.py createsuperuser`
 - Open browser to http://127.0.0.1:8000

---
### Live Demo on Heroku:
 - [django-pastebin-api](https://kbowen-django-pastebin-api.herokuapp.com/)

## Features
 - TBD


---
## Screenshots

### Front page
![Posts](https://github.com/kevinbowen777/pastebin-drf-api/blob/master/images/pastebin_drf_frontpage.png)

### User list
![Profile](https://github.com/kevinbowen777/pastebin-drf-api/blob/master/images/pastebin_drf_users.png)

### Code snippet list
![Profile](https://github.com/kevinbowen777/pastebin-drf-api/blob/master/images/pastebin_drf_snippet_list.png)

### Code snippet detail
![Profile](https://github.com/kevinbowen777/pastebin-drf-api/blob/master/images/pastebin_drf_snippet_detail.png)


---
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/kevinbowen777/pastebin-drf-api/blob/master/LICENSE)
---
### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/pastebin-drf-api/issues)
      to view currently open bug reports or open a new issue.
