from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'chat'

urlpatterns = [
    path('', chat_views, name='index'), 
    path('chatroom/<str:chatroom_name>/', chat_views, name='chatroom'),  
    path('chat/fileupload/<str:chatroom_name>/', chat_file_upload, name='chat-file-upload'),
    path('download/<int:message_id>/', download_file, name='download_file'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
