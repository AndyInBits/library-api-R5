"""Development settings."""

from .common import *
from .common import env

# Base
DEBUG = True

# Security
SECRET_KEY = env('DJANGO_SECRET_KEY',
                 default='django-insecure-ce*lt_q9c!5ka*#8!rkw5x1c51@ojz@)ar+fv(+7k5mod3pb45')

ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# django-extensions
INSTALLED_APPS += ['django_extensions']
