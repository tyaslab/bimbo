from django.conf import settings

import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

SECRET_KEY='th15-15-4-53c123t-k3y'

# If this app is stored at your server, then DEBUG is False
# import socket
# HOSTNAME = '<YOUR_HOST_NAME>'
# DEBUG = socket.gethostname() != HOSTNAME
DEBUG = True # or override its DEBUG status

TEMPLATE_DEBUG = DEBUG # If False, show error messages when error occurs
STATIC_DEBUG = DEBUG # If False, use minimized JS/CSS
DATABASE_DEBUG = DEBUG # If False, should use more 'powerful' database

ALLOWED_HOSTS = ['*']
# INTERNAL_IPS = ()

INSTALLED_APPS = (
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES=(
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
)

ROOT_URLCONF='urls'

# if DATABASE_DEBUG:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         }
#     }
# else:
#     # use more sophisticated sql e.g. MySQL, PostgreSQL, Oracle, etc.
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': '<YOUR_DATABASE_NAME>',
#             'USER': '<YOUR_DATABASE_USERNAME>',
#             'PASSWORD': '<YOUR DATABASE_PASSWORD>',
#             'HOST': '<YOUR_DATABASE_HOST>', # database host
#             'PORT': '3306' # your database port, default is 3306
#         }
#     }

# Internationalization
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_L10N = True

USE_TZ = True

APPEND_SLASH = True

# Static, Media, and Template
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'app/static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'app/media')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'app/templates'),
)

LOGIN_REDIRECT_URL = '/'

TEMPLATE_CONTEXT_PROCESSORS = settings.TEMPLATE_CONTEXT_PROCESSORS + (
   'django.core.context_processors.request',
)

# Mail Configs
SERVER_EMAIL = 'dev@example.com'
DEFAULT_FROM_EMAIL = 'info@example.com'

ADMINS = (
    ('Your Name', 'yourname@example.com'),
)

# example email configuration for mandrill
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'hello@example.com'
EMAIL_HOST_PASSWORD = 'y0u12p455w012dh3r3' # your password here
EMAIL_USE_TLS = True

try:
    from local_settings import *
except ImportError:
    pass