from .base import *

DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = 'django-insecure-@&#k#1(0s549x1%3oqcwj*ask5#i&heh=04jlhm--7h%=z6!2x'

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',

        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'login-api',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',

    }
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    # "AUTHTOKEN",
    "REFRESHTOKEN",
    "content-type"
]
