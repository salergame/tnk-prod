from django.urls import path
from .views import chat_views

app_name = 'chat'

urlpatterns = [
    path('', chat_views, name='index'),  # Основная страница чатов
    path('chatroom/<str:chatroom_name>/', chat_views, name='chatroom'),  # Путь для отдельных чатов
]
