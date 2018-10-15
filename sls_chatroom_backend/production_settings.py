from .settings import *

SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    b'\xd6t>!i\xbbe\x83\xd2\xf6\xf5s&\xbb&\xb8\x8aO%\x96\x92t7\xff\x81Q\xb2#du\xbc\x8b\xbeJw!L=\xe9t.7\xcd\x96\nf\x87\x9e\x8c&T\x16\xe0\x93\x83\x81\xf1\xe83\xdd\xeeK\xffQ\x9a\xa5F:9K\xcf\x0e\x9a\x1b\xfbR\xce\xdb'
)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
DEBUG = False
SECURE_SSL_REDIRECT=True
X_FRAME_OPTIONS='DENY'
SECURE_BROWSER_XSS_FILTER=True
SECURE_SSL_REDIRECT=False
SECURE_CONTENT_TYPE_NOSNIFF=True
SECURE_HSTS_SECONDS=1
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sls_chatroom_backend',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
