"""
    Secrets Example - variables which are not checked into the codebase

    Sensible defaults have been given
"""
import os

try:
    DJANGO_SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
except KeyError:
    DJANGO_SECRET_KEY = 'Your secret key'

try:
    DJANGO_ALLOWED_HOSTS = os.environ['DJANGO_ALLOWED_HOSTS']
except KeyError:
    DJANGO_ALLOWED_HOSTS = []

try:
    DJANGO_DEBUG = os.environ['DJANGO_DEBUG']
except KeyError:
    DJANGO_DEBUG = True

try:
    DATABASE_ENGINE = os.environ['DATABASE_ENGINE']
except KeyError:
    DATABASE_ENGINE = 'django.db.backends.postgresql'

try:
    DATABASE_NAME = os.environ['DATABASE_NAME']
except KeyError:
    DATABASE_NAME = 'database'

try:
    DATABASE_USER = os.environ['DATABASE_USER']
except KeyError:
    DATABASE_USER = 'postgres'

try:
    DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
except KeyError:
    DATABASE_PASSWORD = 'password'

try:
    DATABASE_HOST = os.environ['DATABASE_HOST']
except KeyError:
    DATABASE_HOST = 'localhost'

try:
    DATABASE_PORT = os.environ['DATABASE_PORT']
except KeyError:
    DATABASE_PORT = '5432'
