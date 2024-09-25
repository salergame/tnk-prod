from django.urls import path
from main import views

app_name='main'

urlpatterns = [
    path('',views.index,name='index'),
    path('start-chat/', views.start_chat, name='start_chat'),
    path('chat/<int:chat_id>/', views.chat_with_user, name='chat_with_user'),
    path('staff-chats/', views.staff_chats, name='staff_chats'),
]