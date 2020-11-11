import os
from pathlib import Path
from decouple import config
from dj_database_url import parse as dburl
from logging.handlers import SysLogHandler

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['apsies2020.herokuapp.com', '*', 'localhost']

INSTALLED_APPS = [
    'material.admin',
    'material.admin.default',
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.humanize',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_db_logger',
    'app'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoAdmin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoAdmin.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroku_14853b30fd1f94c',
        'USER': 'b15fa3d88204e8',
        'PASSWORD': 'b1c7130a',
        'HOST': 'us-cdbr-east-06.cleardb.net',
        'PORT': '3306',
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'djangoAdmin',
#        'USER': 'root',
#        'PASSWORD': 'campo123',
#        'HOST': 'localhost',
#        'PORT': '3306',
#    }
#}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'logfile': {
            'class': 'logging.FileHandler',
            'filename': 'server.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['logfile'],
        },
    },
}

#default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

#DATABASES = {'default': config('DATABASE_URL', default=default_dburl, cast=dburl), }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MATERIAL_ADMIN_SITE = {
    'HEADER':  ('APS-2020'),  # Admin site header
    'TITLE':  ('APS-2020'),  # Admin site title
}