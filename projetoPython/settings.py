import os
import shutil
from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

_build_clean_path = BASE_DIR / 'staticfiles'
if _build_clean_path.exists():
    try:
        shutil.rmtree(_build_clean_path)
    except Exception:
        pass

SECRET_KEY = env('SECRET_KEY', default='django-insecure-#!&8h+yu8e2hhze@$%o+5^)7^oa$1ain8ti_u^$ztmxvqxvs*f')
DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = [
    'joaomaia22503478.pw.deisi.ulusofona.pt',
    'localhost',
    '127.0.0.1',
    '.ulusofona.pt',
    'zany-enigma-pjrgr6qx5jr9h7j7j-8000.app.github.dev',
    '.github.dev',
    '.app.github.dev',
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True

CSRF_TRUSTED_ORIGINS = [
    'https://joaomaia22503478.pw.deisi.ulusofona.pt',
    'https://zany-enigma-pjrgr6qx5jr9h7j7j-8000.app.github.dev',
    'https://*.github.dev',
    'https://*.app.github.dev',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]

LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'portfolio:home'
LOGOUT_REDIRECT_URL = 'accounts:login'

INSTALLED_APPS = [
    'cloudinary_storage',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'portfolio',
    'escola',
    'accounts',
    'artigos',
    'markdownify.apps.MarkdownifyConfig',
    'cloudinary',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='joaopedromaia005@gmail.com')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='sbcxlyzialqjluvy')

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER

ROOT_URLCONF = 'projetoPython.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'projetoPython.wsgi.application'

DATABASES = {
    "default": env.db("DATABASE_URL", default="postgresql://neondb_owner:npg_ZY2ofBXIu0ch@ep-wispy-leaf-aq61nu6l-pooler.c-8.us-east-1.aws.neon.tech/neondb?sslmode=require")
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLOUDINARY_CLOUD_NAME', default='dj5ahqraa'),
    'API_KEY': env('CLOUDINARY_API_KEY', default='221665444745343'),
    'API_SECRET': env('CLOUDINARY_API_SECRET', default='6g2NGbLw3iq2EKzsDjIIQOcUjcU'),
}

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

WHITENOISE_MANIFEST_STRICT = False
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MARKDOWNIFY = {
   "default": {
      "WHITELIST_TAGS": [
        'a', 'abbr', 'acronym', 'strong', 'b', 'blockquote', 'em', 'i', 'ul', 'li', 'ol', 'p', 'h1', 'h2', 'h3', 'h4',
      ]
   },
   "alternative": {
      "WHITELIST_TAGS": ["a", "p"],
      "MARKDOWN_EXTENSIONS": ["markdown.extensions.fenced_code",]
   }
}