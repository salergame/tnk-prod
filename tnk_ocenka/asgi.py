"""
ASGI config for tnk_ocenka project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tnk_ocenka.settings')
django.setup()

from django.conf import settings
from django.core.handlers.asgi import ASGIHandler
from whitenoise.asgi import WhiteNoiseMiddleware

django_asgi_app = get_asgi_application()

# Оборачиваем ASGI-приложение в WhiteNoise для обслуживания медиа-файлов
if not settings.DEBUG:
    whitenoise_app = WhiteNoiseMiddleware(django_asgi_app)
    whitenoise_app.add_files(settings.MEDIA_ROOT, prefix=settings.MEDIA_URL.lstrip('/'))
    django_asgi_app = whitenoise_app

application = ProtocolTypeRouter({
    "http": django_asgi_app,
})
