import json
from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from asgiref.sync import async_to_sync
from .models import ChatGroup, GroupMessage

class ChatroomConsumer(WebsocketConsumer):
    def connect(self):
        # Получаем пользователя и имя чата
        self.user = self.scope['user']
        self.chatroom_name = self.scope['url_route']['kwargs']['chatroom_name']
        self.chatroom = get_object_or_404(ChatGroup, group_name=self.chatroom_name)

        # Добавляем пользователя в WebSocket группу (соединение для этой комнаты)
        async_to_sync(self.channel_layer.group_add)(
            self.chatroom_name,
            self.channel_name
        )

        # Добавляем пользователя в список пользователей чата, если его там еще нет
        if not self.chatroom.users_in_chat.filter(id=self.user.id).exists():
            self.chatroom.users_in_chat.add(self.user)

        # Добавляем пользователя в список онлайн
        if not self.chatroom.users_online.filter(id=self.user.id).exists():
            self.chatroom.users_online.add(self.user)
            self.update_online_count()

        # Принимаем соединение WebSocket
        self.accept()

    def disconnect(self, close_code):
        # Отключаем пользователя от WebSocket группы
        async_to_sync(self.channel_layer.group_discard)(
            self.chatroom_name,
            self.channel_name
        )

        # Удаляем пользователя из онлайн-списка ТОЛЬКО при полном разрыве соединения
        if close_code in [1000, 1001]:  # Закрытие соединения
            if self.chatroom.users_online.filter(id=self.user.id).exists():
                self.chatroom.users_online.remove(self.user)
                self.update_online_count()

    def receive(self, text_data):
        # Получаем данные сообщения
        text_data_json = json.loads(text_data)
        body = text_data_json.get('body', '').strip()  # Проверяем, есть ли сообщение и убираем пробелы

        # Проверяем, что сообщение не пустое
        if body:
            # Создаем сообщение в базе данных
            message = GroupMessage.objects.create(
                body=body,
                author=self.user,
                group=self.chatroom
            )

            # Рассылаем сообщение всем участникам комнаты
            event = {
                'type': 'message_handler',
                'message_id': message.id
            }
            async_to_sync(self.channel_layer.group_send)(
                self.chatroom_name, event
            )

    def message_handler(self, event):
        # Получаем сообщение по ID и рендерим его
        message_id = event['message_id']
        message = GroupMessage.objects.get(id=message_id)
        context = {
            'message': message,
            'user': self.user,
        }

        # Отправляем сообщение на фронт
        html = render_to_string('chat/partials/chat_message_p.html', context=context)
        self.send(text_data=html)

    def update_online_count(self):
        # Обновляем количество онлайн пользователей
        online_count = self.chatroom.users_online.count() - 1
        event = {
            'type': 'online_count_handler',
            'online_count': online_count
        }
        async_to_sync(self.channel_layer.group_send)(
            self.chatroom_name, event
        )

    def online_count_handler(self, event):
        # Отправляем обновленное количество пользователей на фронт
        online_count = event['online_count']
        html = render_to_string("chat/partials/online_count.html", {'online_count': online_count})
        self.send(text_data=html)
