from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from map.consumers import EchoConsumer


application = ProtocolTypeRouter({

    # WebSocket handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r"^$", EchoConsumer()),
        ])
    ),
})