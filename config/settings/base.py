import os
import sys
from unipath import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).ancestor(3)
sys.path.append(BASE_DIR.child('apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reusable.apps.ReusableConfig',
    'accounts.apps.AccountsConfig',
    'dashboard.apps.DashboardConfig',
    'levels.apps.LevelsConfig',
    'suscriptions.apps.SuscriptionsConfig',
    'corsheaders',
    'storages',
    'rest_framework',
    'import_export',
    'drf_yasg',
    'raven.contrib.django.raven_compat',
    'django_crontab',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'

AUTHENTICATION_BACKENDS = ['dashboard.helpers.EmailBackend']


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

LOGIN_URL = '/inicio'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# DATABASE_ROUTERS = ['payments.routers.PaymentsRouter']

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]

AUTH_USER_MODEL = 'accounts.User'

# GOOGLE CLOUD STORAGE CONFIG(2018)
BLOB_URL = ''
DEFAULT_FILE_STORAGE = ''
GS_BUCKET_NAME = ''

# MALING SETTINGS
SENDGRID_API_KEY = ''
# EMAIL_HOST = ''
# EMAIL_PORT = 587
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = ''
# EMAIL_USE_SSL = False

# ROUTERS (TO IMPORT OLD DATABASE)
DATABASE_ROUTERS = ['reusable.routers.UsersRouter', ]

# CORS SETTINGS
CORS_ORIGIN_ALLOW_ALL = True

# CELERY SETTINGS
CELERY_BROKER_URL = 'redis://localhost:6379'

# OPENPAY SETTINGS
OPENPAY_API_KEY_SANDBOX = ''
OPENPAY_API_KEY_PUBLIC_SANDBOX = ''
OPENPAY_MERCHANT_ID_SANDBOX = ''

# SANDBOX PLANS
OPENPAY_PLAN_1_SANDBOX = ''
OPENPAY_PLAN_2_SANDBOX = ''
OPENPAY_PLAN_3_SANDBOX = ''

OPENPAY_API_KEY = ''
OPENPAY_MERCHANT_ID = ''
OPENPAY_API_KEY_PUBLIC = ''

OPENPAY_PLAN_1 = ''
OPENPAY_PLAN_2 = ''
OPENPAY_PLAN_3 = ''
OPENPAY_PLAN_4 = ''
OPENPAY_PLAN_5 = ''
OPENPAY_PLAN_6 = ''
OPENPAY_PLAN_7 = ''
OPENPAY_PLAN_8 = ''
OPENPAY_PLAN_9 = ''
OPENPAY_PLAN_10 = ''


CRONJOBS = [
    ('10 1 * * *', 'levels.cron.restart_active_missions', '>> /tmp/cron_active_missions.log')
]