"""
WSGI config for tnk_ocenka project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.conf import settings
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tnk_ocenka.settings')

application = get_wsgi_application()

# Добавляем медиа-файлы к обслуживаемым файлам через WhiteNoise
if not settings.DEBUG:
    application = WhiteNoise(application)
    application.add_files(settings.MEDIA_ROOT, prefix=settings.MEDIA_URL.lstrip('/'))
