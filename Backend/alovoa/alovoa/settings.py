"""
Django settings for alovoa project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from django.contrib import admin

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#(a-veg9k!_*(87thhss!y5_v+mzfzc)r33kwo@ifo3yj+&mlh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['139.84.135.154','*']
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://anotherdomain.com"
]


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user_accounts',
    'rest_framework',
    'corsheaders',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware'
]

ROOT_URLCONF = 'alovoa.urls'

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

WSGI_APPLICATION = 'alovoa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'defaultdb',
        'USER': 'vultradmin',
        'PASSWORD': 'AVNS_WrhUuPNF0MNwMNnWFy5',
        'HOST': 'vultr-prod-2f6feb88-520b-4806-bec9-fe81d0f8ec0f-vultr-prod-5d43.vultrdb.com',
        'PORT': '16751',
    }
}


class CustomAdminSite(admin.AdminSite):
    site_header = "Ameotech Admin"
custom_admin_site = CustomAdminSite()

JAZZMIN_SETTINGS = {
    "site_title": "Admin Panel",
}





# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIR = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # Directory where uploaded media is saved.
MEDIA_URL = '/media/' # Public URL at the browser

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field




DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'user_accounts.CustomUser'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # Change this as needed for your project's security requirements
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}

CORS_ALLOW_ALL_ORIGINS = True  # Set this to True to allow all origins, use it carefully in production.
CORS_ALLOW_CREDENTIALS = True  # Set this to True if your API uses cookies or authentication.


# Specify the HTTP methods and headers that are allowed in cross-origin requests.
CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

STRIPE_PUBLIC_KEY = 'pk_test_51NfjzOSA1sOBZbZTKvOc1PHFkMYgufgopdqvT1UKkwrlZp7O8rdJQnk7UMPzom20CjPrwuQxqexQKa3oMPqQPoC500C3FrDN6Q'
STRIPE_SECRET_KEY = 'sk_test_51NfjzOSA1sOBZbZTwjWW0fEO1FrsqzhXG1JKH4FcqjfY1rCmVqhiYOJu12eWgKPnXJxb25apkDCvowya3hHJdAFe009euYRZZ2'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'defaultdb',
        'USER': 'vultradmin',
        'PASSWORD': 'AVNS_WrhUuPNF0MNwMNnWFy5',
        'HOST': 'vultr-prod-2f6feb88-520b-4806-bec9-fe81d0f8ec0f-vultr-prod-5d43.vultrdb.com',
        'PORT': '16751',
    }
}
