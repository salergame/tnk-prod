"""
WSGI config for tnk_ocenka project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import mimetypes
from django.core.wsgi import get_wsgi_application
from django.conf import settings
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tnk_ocenka.settings')

application = get_wsgi_application()

# Добавляем медиа-файлы к обслуживаемым файлам через WhiteNoise
if not settings.DEBUG:
    # Регистрируем дополнительные MIME-типы для медиа-файлов
    mimetypes.add_type('image/jpeg', '.jpg')
    mimetypes.add_type('image/jpeg', '.jpeg')
    mimetypes.add_type('image/png', '.png')
    mimetypes.add_type('application/pdf', '.pdf')
    mimetypes.add_type('application/msword', '.doc')
    mimetypes.add_type('application/vnd.openxmlformats-officedocument.wordprocessingml.document', '.docx')
    
    application = WhiteNoise(application, root=settings.STATIC_ROOT)
    # Добавляем медиа-файлы с правильным префиксом
    application.add_files(settings.MEDIA_ROOT, prefix=settings.MEDIA_URL.lstrip('/'))
