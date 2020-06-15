from .settings_base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eszm$#b$cav^q&qihd6cv8xmej!c&39u_=l0$kxy_gbft$i$$-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES['default']['NAME'] = 'django_akaman'
DATABASES['default']['USER'] = 'root'
DATABASES['default']['PASSWORD'] = 'root'
DATABASES['default']['HOST'] = '127.0.0.1'
DATABASES['default']['PORT'] = '3306'

