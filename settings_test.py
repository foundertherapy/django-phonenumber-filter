INTERNAL_IPS = ('127.0.0.1', )
ALLOWED_HOSTS = ['localhost', '127.0.0.1', ]
APPEND_SLASH = True
TIME_ZONE = 'UTC'
USE_TZ = True
SECRET_KEY = 'abc'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django_coverage',
    'phonenumber_filter',
)

