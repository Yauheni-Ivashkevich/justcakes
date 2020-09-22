import os
from pathlib import Path

import dj_database_url
from dynaconf import settings as _settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
CORE_DIR = Path(__file__).parent.resolve()  # /core
BASE_DIR = CORE_DIR.parent.resolve()  # /src
REPO_DIR = BASE_DIR.parent.resolve()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = _settings.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = _settings.DEBUG

ALLOWED_HOSTS = _settings.ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",  # отвечает за админку
    "django.contrib.auth",  # отвечает за управление пользователями
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # ---applications---
    "applications.index",
    # 'applications.range',
    "applications.checkout",
    "applications.contacts",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Heroku по умолчанию не отдаёт staticfiles. Для использовать whitenoise.
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = "core.urls"  # все urls беруться здесь

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [CORE_DIR / "templates"],  # здесь находятся шаблоны
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Heroku: Update database configuration from $DATABASE_URL.
_db_url = _settings.DATABASE_URL
if _settings.ENV_FOR_DYNACONF == "heroku":
    _db_url = os.getenv("DATABASE_URL")

DATABASES = {"default": dj_database_url.parse(_db_url, conn_max_age=600)}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/assets/"

STATICFILES_DIRS = [CORE_DIR / "static"]

STATIC_ROOT = REPO_DIR / ".static"

# STATIC_URL = '/assets/'
# STATIC_DIR = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [STATIC_DIR]


"""В apps добавить приложение storages и добавить переменные 
DROPBOX_OAUTH2_TOKEN и DROPBOX_ROOT_PATH.
settings.py"""
# INSTALLED_APPS = (
#     ...
#     'storages',
#     ...
# )
# DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
# DROPBOX_OAUTH2_TOKEN='your token'
# DROPBOX_ROOT_PATH='your path'

"""Обновить загруженный файл в хранилище можно следующим образом"""
# from storages.backends.dropbox import DropboxStorage
# from dropbox.files import WriteMode
#
# dbx = DropBoxStorage(settings.DROPBOX_OAUTH2_TOKEN)
# mode = WriteMode.overwrite
# name = instance.file.file.name
# dbx.client.files_upload(bytes(data, 'utf-8'), name, mode)
"""https://istroev.me/django-dropbox-storage/""" 