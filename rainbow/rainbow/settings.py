
import django_heroku
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '+m$s)u%0#lb-!v&ci*_hqob+-lp_!mb(1zpi0wr0lqta@r*3$k'


DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    #apps
    'main',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'storages',
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

ROOT_URLCONF = 'rainbow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'rainbow.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True






STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static_cdn','static_root')


MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static_cdn","media_root")


#AWS configuration

AWS_ACCESS_KEY_ID = 'AKIARUGQXMPZP2QKGHCE'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'publicrootkings'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_S3_FILE_OVERWRITE = False
AWS_LOCATION = 'static'

#for static
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#for media
DEFAULT_FILE_STORAGE = 'rainbow.storage_backends.MediaStorage' 


django_heroku.settings(locals())

#database config

import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

#sendgrid

SENDGRID_API_KEY = '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'
# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_HOST_USER = 'jidnyeshaj'
# EMAIL_HOST_PASSWORD = 'sendgrid1234'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'jidnyeshaj@gmail.com'
# ACCOUNT_EMAIL_SUBJECT_PREFIX = 'rainbowcreations'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'