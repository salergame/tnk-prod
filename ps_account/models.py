from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings
from django.urls import reverse

def get_document_path(instance, filename):
    # Сохраняем файл в папку media/documents/ с именем файла
    return os.path.join('documents', filename)

def get_avatar_path(instance, filename):
    # Сохраняем аватар в папку media/avatars/ с именем файла
    return os.path.join('avatars', filename)

class UserDocument(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.FileField(upload_to=get_document_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.document.name}"

    def get_document_url(self):
        if self.document and hasattr(self.document, 'url'):
            # Получаем только имя файла из полного пути
            filename = os.path.basename(self.document.name)
            # Используем представление serve_document из корневых URL
            return reverse('serve_document_root', kwargs={'filename': filename})
        return None

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=get_avatar_path, null=True, blank=True)

    def __str__(self):
        return self.user.username

    def get_avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url') and self.avatar.name:
            # Получаем только имя файла из полного пути
            filename = os.path.basename(self.avatar.name)
            # Используем представление serve_avatar из корневых URL
            return reverse('serve_avatar_root', kwargs={'filename': filename})
        return None

