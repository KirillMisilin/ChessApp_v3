from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
    re_path(r'ws/socket-server/play/', consumers.ChessConsumer.as_asgi()),
    re_path(r'ws/socket-server/', consumers.FindGameConsumer.as_asgi())
]