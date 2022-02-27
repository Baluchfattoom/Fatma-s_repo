"""
Django settings for cpims project.

Generated by 'django-admin startproject' using Django 1.8.4.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'h34yo5l8c8!edb%^b@3j-i^gc$e)fcjnw_9jm4a^%jbq&*41+@'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'cpovc_auth',
    'cpovc_registry',
    'cpovc_main',
    'cpovc_forms',
    'cpovc_gis',
    'cpovc_access',
    'cpovc_ovc',
    'cpovc_settings',
    'cpovc_manage',
    'cpovc_reports',
    'cpovc_help',
    'notifications',
    'crispy_forms',
    'rest_framework',
    'rest_framework.authtoken',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'cpovc_access.middleware.AuthenticationPolicyMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'cpovc_main.middleware.SqlPrintingMiddleware',
    'cpovc_auth.middleware.UserRestrictMiddleware',
    'cpovc_access.middleware.FailedLoginMiddleware',
)

ROOT_URLCONF = 'cpims.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR, 'templates')), ],
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

WSGI_APPLICATION = 'cpims.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cpims',
        'USER': 'cpimsdbuser',
        'PASSWORD': 'Xaen!ee8',
        'HOST': '127.0.0.1',
        'PORT': '5435', }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DOCUMENTS_URL = '/documents/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'reports')

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )

AUTH_USER_MODEL = 'cpovc_auth.AppUser'

AUTHENTICATION_BACKENDS = ('cpovc_auth.backends.CPOVCAuthenticationBackend',)

ALLOW_NATIONAL_ID_LOGIN = True

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# to find out what this does
IS_CAPTURE_SITE = False

GIT_ROOT = ''

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'cpimskenya@gmail.com'
EMAIL_HOST_PASSWORD = 'WHfJk5F4eKutLQ6'

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER

# Session variables
SESSION_COOKIE_AGE = 3 * 60 * 60
SESSION_SAVE_EVERY_REQUEST = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

AXES_LOCKOUT_TEMPLATE = 'locked.html'
AXES_COOLOFF_TIME = 0.25

PASSWORD_CHANGE_POLICIES = (
    ('cpovc_access.password_change.PasswordChangeExpired', {}),
    ('cpovc_access.password_change.PasswordChangeTemporary', {}),
)

PASSWORD_STRENGTH_POLICIES = (
    ('cpovc_access.password_strength.PasswordMinLength', {}),
    ('cpovc_access.password_strength.PasswordContainsUpperCase', {}),
    ('cpovc_access.password_strength.PasswordContainsLowerCase', {}),
    ('cpovc_access.password_strength.PasswordContainsNumbers', {}),
    ('cpovc_access.password_strength.PasswordContainsSymbols', {}),
    ('cpovc_access.password_strength.PasswordUserAttrs', {}),
    ('cpovc_access.password_strength.PasswordLimitReuse', {}),
    ('cpovc_access.password_strength.PasswordDisallowedTerms', {
        'terms': ['cpims']
    }),
)

AUTHENTICATION_POLICIES = (
    ('cpovc_access.authentication.AuthenticationBasicChecks', {}),
    ('cpovc_access.authentication.AuthenticationDisableExpiredUsers', {}),
)

DOCUMENT_ROOT = os.path.join(BASE_DIR, 'templates/documents')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
CSRF_FAILURE_VIEW = 'cpims.views.csrf_failure'
