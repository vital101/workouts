from workouts.settings.base import *
import dj_database_url
import os

DEBUG = True

COMPRESS_OFFLINE = False
COMPRESS_ENABLED = False

SECURE_SSL_REDIRECT = True

ALLOWED_HOSTS = [
    "workouts.re-cycledair.com"
]

DATABASES['default'] = dj_database_url.config(
    conn_max_age=600,
    conn_health_checks=True,
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': os.environ['REDIS_URL'],
    }
}

print('Using production.py settings...')
