# SLS-Chatroom backend

## Django Rest Framework api for [SLS-Chatroom](https://github.com/stevenlsjr/sls-chatroom)

## Installation

```bash
$ git clone https://github.com/stevenlsjr/sls_chatroom_backend.git
$ cd sls_chatroom_backend
# Optional: Create virtualenv for project
$ virtualenv -p $(which python3) env && source env/bin/activate
$ pip install -r requirements.txt
```

Setup database according to [Django Database settings](https://docs.djangoproject.com/en/2.1/ref/settings/#databases)

```bash
$ python manage.py migrate
```

Run in development mode

```bash
$ DJANGO_SETTINGS_MODULE=$YOUR_LOCAL_SETTINGS_MODULE python manage.py runserver
```
