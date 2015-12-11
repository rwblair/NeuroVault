DEBUG = False
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_NAME', ''),
        'USER': os.environ.get('POSTGRES_USER', ''),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
        'HOST': os.environ.get('POSTGRES_HOST', ''),
        'PORT': os.environ.get('POSTGRES_PORT', ''),
    }
}

INSTALLED_APPS += (
    "opbeat.contrib.django",
)
OPBEAT = {
    "ORGANIZATION_ID": "",
    "APP_ID": "",
    "SECRET_TOKEN": ""
}
MIDDLEWARE_CLASSES += (
    'opbeat.contrib.django.middleware.OpbeatAPMMiddleware',
)
