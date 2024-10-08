"""
Django settings for djangocrud project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

# Importar os para manejar las variables de entorno
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from dotenv import load_dotenv
from djangocrud.local_settings import IS_DEPLOYED, DATABASE_DICT
from djangocrud.logging_settings import *
from djangocrud.cloud_settings import *

# Carga las variables de entorno del archivo .env
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Construir rutas dentro del proyecto de esta manera: BASE_DIR / 'subdir'.
# from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(oa(omhdw75#3qzk_p-6zfdfmvj#%tn=oci!ww+ssog(ib%-o='

# SECURITY WARNING: don't run with debug turned on in production!
# Seguridad: no ejecute con depuración activada en producción!
# Se recomienda que DEBUG sea False en producción
# Se recomienda que DEBUG sea True en desarrollo
DEBUG = not IS_DEPLOYED

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0:8080', 'usuarios-tasks.up.railway.app']

CSRF_TRUSTED_ORIGINS = ['http://*', 'https://usuarios-tasks.up.railway.app']  

# Application definition
# Definición de aplicaciones

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'whitenoise.runserver_nostatic',
    'storages',
    'tasks'
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


# URL Configuration
# Configuración de URL
# https://docs.djangoproject.com/en/4.1/topics/http/urls/
ROOT_URLCONF = 'djangocrud.urls'

# Template Configuration
# Configuración de plantillas
# https://docs.djangoproject.com/en/4.1/topics/templates/
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

# WSGI Configuration
# Configuración de WSGI
WSGI_APPLICATION = 'djangocrud.wsgi.application'


# Database
# Configuración de la base de datos
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': DATABASE_DICT
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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'
# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static files (CSS, JavaScript, Images)
# Archivos estáticos (CSS, JavaScript, imágenes)
# Configura la ruta de los archivos estáticos
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/staticfiles/' if IS_DEPLOYED else '/static/'

LOGIN_URL = '/signin'

"""
# Configuración para almacenar archivos estáticos en S3
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
"""

# Configuración para almacenar archivos multimedia en el sistema de archivos (S3)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if not IS_DEPLOYED:
    MEDIA_URL = '/media/'
else:
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'
    
# Se define el nombre de la carpeta de archivos públicos para almacenar las imágenes de las caratulas de los libros
PUBLIC_MEDIA = 'publico'
