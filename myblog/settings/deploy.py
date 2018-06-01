from .common import *

DEBUG = True

INSTALLED_APPS += ['debug_toolbar']

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'myblog', 'static'),
]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ALLOWED_HOSTS = ['*']

MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware',]