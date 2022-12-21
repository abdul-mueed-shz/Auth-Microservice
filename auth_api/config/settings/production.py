from .base import *

DEBUG = False

ALLOWED_HOSTS = []

SECRET_KEY = ''  # set using .env

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
