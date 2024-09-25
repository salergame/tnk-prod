# routing.py
from django.urls import re_path
from tnk_ocenka.consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_id>\d+)/$', ChatConsumer.as_asgi()),
]

# urls.py
from django.urls import path
from ps_account.views import start_chat, chat_room, staff_chat_list

urlpatterns = [
    path('start-chat/', start_chat, name='start_chat'),
    path('chat/<int:room_id>/', chat_room, name='chat_room'),
    path('staff-chats/', staff_chat_list, name='staff_chat_list'),
]
