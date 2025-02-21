"""
ASGI config for engine project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
import django
from channels.routing import get_default_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "engine.settings")
django.setup()
application = get_default_application()


application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests

    # WebSocket chat handler
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path("chat/admin/", AdminChatConsumer.as_asgi()),
                path("chat/", PublicChatConsumer.as_asgi()),
            ])
        )
    ),
})