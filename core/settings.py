from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-0*cr9siyt1%cead+5gz77oiws%$$+oq6di$or6m#gvl@dtsjv!'
DEBUG = True

ALLOWED_HOSTS = ['docplow.cf', '134.209.145.42']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentication',
    'home',
    'idgenerator',
    'django_bootstrap5',
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mrplow_db',
        'USER': 'mrplow',
        'PASSWORD': 'q1dhN0eD',
        'HOST': 'localhost',
        'PORT': '5432',
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
LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATA_UPLOAD_MAX_NUMBER_FIELDS = 103400


#
#
#
#
# #CRYPTO PAYMENT SETUP
# CRYPTOCURRENCY_PAYMENT = {
#     "BITCOIN": {
#         "CODE": "btc",
#         "BACKEND": "merchant_wallet.backends.btc.BitcoinBackend",
#         "FEE": 0.00,
#         "REFRESH_PRICE_AFTER_MINUTE": 15,
#         "REUSE_ADDRESS": False,
#         "ACTIVE": True,
#         "MASTER_PUBLIC_KEY": 'PUT_YOUR_WALLET_MASTER_PUBLIC_KEY',
#         "CANCEL_UNPAID_PAYMENT_HRS": 24,
#         "CREATE_NEW_UNDERPAID_PAYMENT": True,
#         "IGNORE_UNDERPAYMENT_AMOUNT": 10,
#         "IGNORE_CONFIRMED_BALANCE_WITHOUT_SAVED_HASH_MINS": 20,
#         "BALANCE_CONFIRMATION_NUM": 1,
#         "ALLOW_ANONYMOUS_PAYMENT": True,
#     }
#  }
# ORGS_SLUGFIELD = 'django_extensions.db.fields.AutoSlugField'
# ORGS_SLUGFIELD = 'autoslug.fields.AutoSlugField'
INTERNAL_IPS = ['193.111.48.56']
LOGIN_REDIRECT_URL = "home"  # Route defined in home/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in home/urls.py
