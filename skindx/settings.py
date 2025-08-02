from pathlib import Path

# --------------------------------------------------
# Basic Setup
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-e=xvm@k9k3jkns(zpkf7(6oj8n61qr4rf-diy$t1b06jfdxvri'
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# --------------------------------------------------
# CSRF for SSLCommerz
# --------------------------------------------------

CSRF_TRUSTED_ORIGINS = [
    "https://sandbox.sslcommerz.com",
    "https://securepay.sslcommerz.com",
]

# --------------------------------------------------
# Installed Apps
# --------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'core.apps.CoreConfig',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

# --------------------------------------------------
# Middleware
# --------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'skindx.urls'

# --------------------------------------------------
# Templates
# --------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'core/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'skindx.wsgi.application'

# --------------------------------------------------
# MySQL Database Configuration
# --------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'skindx',
        'USER': 'root',
        'PASSWORD': '',  # Set your MySQL password if any
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# --------------------------------------------------
# Password Validation
# --------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --------------------------------------------------
# Time & Language
# --------------------------------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_TZ = True
USE_I18N = True
USE_TZ = True

# --------------------------------------------------
# Static & Media Files
# --------------------------------------------------

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'core/static']
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --------------------------------------------------
# Django Defaults
# --------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SITE_ID = 1

# --------------------------------------------------
# Allauth Login Settings (no username)
# --------------------------------------------------

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

ACCOUNT_LOGIN_METHODS = {'email'}
ACCOUNT_SIGNUP_FIELDS = ['email*', 'password1*', 'password2*']

# --------------------------------------------------
# SSLCommerz Configuration
# --------------------------------------------------


SSLCOMMERZ = {
    'store_id': 'solvo68849db11c233',
    'store_pass': 'solvo68849db11c233@ssl',
    'sandbox': True
}

# --------------------------------------------------
# Social Account Providers
# --------------------------------------------------

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'https://www.googleapis.com/auth/userinfo.email',
            'https://www.googleapis.com/auth/userinfo.profile',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}