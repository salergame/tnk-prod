from django.db import models
from django.contrib.auth.models import User


class ChatGroup(models.Model):
    group_name = models.CharField(max_length=128, unique=True, blank=True)
    users_online = models.ManyToManyField(User, related_name='online_in_groups', blank=True)
    users_in_chat = models.ManyToManyField(User, related_name='users_in_groups', blank=True)
    # Для реализации приватных чатов добавим следующие поля
    other_user = models.ForeignKey(User, related_name='private_chat_user', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.group_name

class GroupMessage(models.Model):
    group = models.ForeignKey(ChatGroup, related_name='chat_messages', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=300, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        if self.body:
            return f'{self.author.username}: {self.body}'
        else:
            return f'{self.author.username}: [empty message]'
        
    class Meta:
        ordering = ['-created']