from .base import *
from decouple import config
from environ import Env, Csv  

# Debug settings
DEBUG = config('DEBUG', default=True, cast=bool)

# Security
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=Csv())

CORS_ALLOW_ALL_ORIGINS = True  # For development only

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'x_tracker'),
        'USER': os.environ.get('POSTGRES_USER', 'x_tracker'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'x_tracker'),
        'HOST': os.environ.get('POSTGRES_HOST', 'db'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}

# Initialize environment
env = Env()
env.read_env()

# Celery
CELERY_BROKER_URL = config('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = config('CELERY_RESULT_BACKEND')

# Email settings (development)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'