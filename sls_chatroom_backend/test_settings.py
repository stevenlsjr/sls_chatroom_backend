from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres_test',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PORT': 5434,
    }
}
