from .base import *

ALLOWED_HOSTS = ['*']

DEBUG = True

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django_secret_key')

TRIM_API_URL = os.environ.get('TRIM_API_URL', 'https://dev.mycar.cardoc.co.kr/v1/trim')

MAX_REGISTRATION_TIRE_COUNT = os.environ.get('MAX_REGISTRATION_TIRE_CONUT', 5)

SIMPLE_JWT['SIGNING_KEY'] = SECRET_KEY

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('SQL_DATABASE_NAME', 'cardoc_local_dev'),
        'USER': os.environ.get('SQL_USER', 'cardoc_local_dev'),
        'PASSWORD': os.environ.get('SQL_PASSWORD', 'cardoc_local_dev'),
        'HOST': os.environ.get('SQL_HOST', 'localhost'),
        'PORT': os.environ.get('SQL_PORT', 5432),
    }
}