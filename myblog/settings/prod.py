from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# 실 서비스 도메인 입력
ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'myblog', 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'staticfiles')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')
