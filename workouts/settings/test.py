from workouts.settings.base import *

DEBUG = True
COMPRESS_OFFLINE = False
COMPRESS_ENABLED = False
SECURE_SSL_REDIRECT = False

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

print('Using test.py settings...')
