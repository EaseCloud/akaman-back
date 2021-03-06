from django_base.base_settings import *

"""
Django settings for akaman project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

ROOT_URLCONF = 'core.urls'

INSTALLED_APPS += [
    'django_base.base_config',
    'django_base.base_media',
    'core',
]

WSGI_APPLICATION = 'akaman.wsgi.application'
