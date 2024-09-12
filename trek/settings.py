"""
Django settings for cnex project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import platform
server_type = "AWS"#"LOCAL"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

current_os = platform.system()

if current_os == "Linux" and server_type == "AWS":
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env') #server env
else:
    dotenv_path = os.path.join(os.path.dirname(__file__), 'env_local') #this is local env
load_dotenv(dotenv_path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = [host for host in os.getenv('ALLOWED_HOSTS').split(',') if host != '']

# Application definition
# settings.py

# settings.py

FILE_UPLOAD_MAX_MEMORY_SIZE = 850 * 1024 * 1024  # 850 MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 850 * 1024 * 1024  # 850 MB



INSTALLED_APPS = [
    # 'daphne',
    # 'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'drf_yasg',
    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters',
    'accounts',
    'managements',
    'destination',
    'services',
    'booking',
    'payment',
    'queries',
    'review',
    'dashboard',
    'accountsmanagement',
    'setupemail',
    'collection',
    'activities',
    'faqs',
    'departure',
    'company',
    'blog',
    'airlines',
    'gallery',
    'report',
]

# ASGI_APPLICATION = 'trek.asgi.application'
AUTH_USER_MODEL = 'accounts.CustomUser'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = [white for white in os.getenv('CORS_ORIGIN_WHITELIST').split(',') if white != '']
CSRF_TRUSTED_ORIGINS = [trusted for trusted in os.getenv('CSRF_TRUSTED_ORIGINS').split(',') if trusted != '']

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # static file serving.
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'trek.urls'

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

WSGI_APPLICATION = 'trek.wsgi.application'

# Database
#https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DATABASE_ENGINE'),
        'NAME': os.getenv('DATABASES_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    # 'accounts.backend.EmailserBackend',
]
# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


import os
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'https://api.everestthrills.com/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
MEDIA_URL = 'https://api.everestthrills.com/media/'

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# MEDIA_URL = 'https://api.everestthrills.com/media/'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CORS_ORIGIN_ALLOW_ALL = True #if True then allow only for whitelist ip.(frontend request)
CORS_ORIGIN_WHITELIST = [white for white in os.getenv('CORS_ORIGIN_WHITELIST').split(',') if white != '']
CSRF_TRUSTED_ORIGINS = [trusted for trusted in os.getenv('CSRF_TRUSTED_ORIGINS').split(',') if trusted != '']


from datetime import timedelta

# SIMPLE_JWT = {
#     "ACCESS_TOKEN_LIFETIME": timedelta(days=7),
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
#     "ROTATE_REFRESH_TOKENS": False,
#     "BLACKLIST_AFTER_ROTATION": False,
#     "UPDATE_LAST_LOGIN": False,

#     "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
# }
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    # "MAX_PAGE_SIZE": 1
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=50),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "AUTH_HEADER_TYPES": ("Bearer", "JWT"),
    # "USER_ID_FIELD": "id",
    # "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
}

# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'manojdas.py@gmail.com'
# EMAIL_HOST_PASSWORD = 'qizi zhwj urhp vmvv'

EMAIL_BACKEND = 'setupemail.utilities.custom_email_setup_backend.CustomEmailBackend'

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

SMS_KEY_PASSWORD = ''

