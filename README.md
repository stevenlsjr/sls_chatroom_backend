# SLS-Chatroom backend

## Django rest Framework api for [SLS-Chatroom](https://github.com/stevenlsjr/sls-chatroom)

[![Build Status](https://travis-ci.org/stevenlsjr/sls_chatroom_backend.svg?branch=master)](https://travis-ci.org/stevenlsjr/sls_chatroom_backend)

### Dependencies:

Python 3.x, Postgresql.

### Instalation and running

Inside of a virtualenv, exec:

```bash
$ pip install -r requirements.txt
```

Run migrations and create superuser via:

```bash
$ ./manage.py migrate
$ ./manage.py createsuperuser
```

Run the development server with:

```bash
$ ./manage.py runserver $HOST_URL_HERE
```

### Testing

run `pytest`
