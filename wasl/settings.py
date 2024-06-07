"""

Django settings for wasl project.


Generated by 'django-admin startproject' using Django 5.0.


For more information on this file, see

https://docs.djangoproject.com/en/5.0/topics/settings/


For the full list of settings and their values, see

https://docs.djangoproject.com/en/5.0/ref/settings/

"""


from pathlib import Path
import os




# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production

# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'django-insecure-tzk#pg6@@voz+am_@pqz85(cl!k6-+f1=w625z*+fe7$5&km!0'


# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True





# إعدادات محلية (يمكن تغييرها في التطوير)
try:
    from .local_settings import DATABASES
except ImportError:
    pass



ALLOWED_HOSTS = []



# Application definition


INSTALLED_APPS = [

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',

    'The_Owner',

    'The_Investor',
    
    'FM',

    'Chat',
    
    'page',

    'accounts',

 


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


ROOT_URLCONF = 'wasl.urls'


TEMPLATES = [

    {

        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [os.path.join(BASE_DIR , 'templates')],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.debug',

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',

                'The_Owner.context_processors.unread_messages_count',

            ],

        },

    },

]


WSGI_APPLICATION = 'wasl.wsgi.application'



# Database

# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': BASE_DIR / 'db.sqlite3',


    }

}



# Password validation

# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators


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

# https://docs.djangoproject.com/en/5.0/topics/i18n/



LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Aden'
USE_TZ = True
USE_I18N = True




# Static files (CSS, JavaScript, Images)

# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR , 'wasl/static'),

]

#MEDIA-----------------------------
# # settings.py

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'
    
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Default primary key field type

# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # أو ملف


from django.contrib.messages import constants as messages
from django.contrib.messages import constants as messages_constants

#messages
MESSAGE_TAGS = {
    messages_constants.ERROR: 'danger',
    messages_constants.DEBUG: 'debug',
    messages_constants.INFO: 'info',
    messages_constants.SUCCESS: 'success',
    messages_constants.WARNING: 'warning',
}





# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 1025
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL = False


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025



