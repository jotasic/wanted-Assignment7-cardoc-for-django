from .base import *

ALLOWED_HOSTS = ['*']

DEBUG = True

SECRET_KEY = get_env_variable('DJANGO_SECRET_KEY')

SIMPLE_JWT['SIGNING_KEY'] = SECRET_KEY

DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.postgresql',
        'NAME'    : get_env_variable('SQL_DATABASE_NAME'),
        'USER'    : 'postgres',
        'PASSWORD': get_env_variable('SQL_PASSWORD'),
        'HOST'    : get_env_variable('SQL_HOST'),
        'PORT'    : get_env_variable('SQL_PORT'),
    }
}