
import os from pathlib 
import Path from dotenv 
import load_dotenv 
import dj_database_url

load_dotenv()

BASE_DIR = Path(file).resolve().parent.parent


SECRET_KEY = os.getenv("SECRET_KEY", "clave-insegura-dev")
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost").split(",")


INSTALLED_APPS = [ 'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles', 'productos',

# Allauth
'django.contrib.sites',
'allauth',
'allauth.account',
'allauth.socialaccount',
'allauth.socialaccount.providers.google',

]

SITE_ID = 1

MIDDLEWARE = [ 'django.middleware.security.SecurityMiddleware', 'django.contrib.sessions.middleware.SessionMiddleware', 'django.middleware.common.CommonMiddleware', 'django.middleware.csrf.CsrfViewMiddleware', 'django.contrib.auth.middleware.AuthenticationMiddleware', 'django.contrib.messages.middleware.MessageMiddleware', 'django.middleware.clickjacking.XFrameOptionsMiddleware', 'allauth.account.middleware.AccountMiddleware', ]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [ { 'BACKEND': 'django.template.backends.django.DjangoTemplates', 'DIRS': [BASE_DIR / 'templates'], 'APP_DIRS': True, 'OPTIONS': { 'context_processors': [ 'django.template.context_processors.request', 'django.contrib.auth.context_processors.auth', 'django.contrib.messages.context_processors.messages', ], }, }, ]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = { 
    'default': dj_database_url.config( default=os.getenv('DATABASE_URL'), 
    conn_max_age=600, ssl_require=True) 
}

AUTH_PASSWORD_VALIDATORS = [ {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'}, {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'}, {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'}, {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}, ]

LANGUAGE_CODE = 'en-us' 
TIME_ZONE = 'UTC' 
USE_I18N = True 
USE_TZ = True


STATIC_URL = '/static/' 
STATIC_ROOT = BASE_DIR / 'staticfiles' 
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/' 
MEDIA_ROOT = BASE_DIR / 'media'

EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend') 
EMAIL_HOST = os.getenv("EMAIL_HOST", "") 
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587)) 
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True") == "True" 
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "") 
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "") 
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

AUTHENTICATION_BACKENDS = [ 'django.contrib.auth.backends.ModelBackend', 'allauth.account.auth_backends.AuthenticationBackend', ]
