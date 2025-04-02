from django.urls import re_path
from .consumers import HostPanelConsumer, GameBoardConsumer

websocket_urlpatterns = [
    re_path(r"ws/host_panel/$", HostPanelConsumer.as_asgi()),
    re_path(r"ws/game_board/$", GameBoardConsumer.as_asgi()),
]
