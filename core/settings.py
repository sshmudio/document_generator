from django.contrib.messages import constants as message_constants
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-0*cr9siyt1%cead+5gz77oiws%$$+oq6di$or6m#gvl@dtsjv!'
DEBUG = False
MESSAGE_LEVEL = message_constants.DEBUG
ALLOWED_HOSTS = ['docplow.cf', '167.71.61.95']

INSTALLED_APPS = [
    'django.contrib.admin',
    'authentication',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'bootstrap5',
    'wallets',
    'django_bootstrap5',
    'djmoney',
    'django_user_agents',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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
        'NAME': 'documents_db',
        'USER': 'documentor',
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

USE_L10N = False


USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATA_UPLOAD_MAX_NUMBER_FIELDS = 103400
LOGIN_REDIRECT_URL = "home"  # Route defined in home/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in home/urls.py
INTERNAL_IPS = [
    '93.73.62.199',
]

# AUTH_USER_MODEL = 'authentication.MyUser'

# CRYPTO SETTINGS


# Cache backend is optional, but recommended to speed up user agent parsing


# Name of cache backend to cache user agents. If it not specified default
# cache alias will be used. Set to `None` to disable caching.
USER_AGENTS_CACHE = 'default'
