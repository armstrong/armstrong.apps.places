from armstrong.dev.tasks import *

settings = {
    'INSTALLED_APPS': (
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'armstrong.apps.places',
        'armstrong.apps.places.tests.places_support',
        'armstrong.core.arm_content',
    ),
    'TEMPLATE_CONTEXT_PROCESSORS': (
        'django.core.context_processors.request',
    ),
    'ROOT_URLCONF': 'armstrong.apps.places.urls',
    'SITE_ID': 1,
}

main_app = 'places'
tested_apps = (main_app,)
