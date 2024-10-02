from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required
from .models import ChatGroup, GroupMessage
from .forms import ChatmessageCreateForm

from django.contrib.auth.models import User
from django.db.models import Q
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils.crypto import get_random_string

@login_required
def chat_views(request, chatroom_name="public-chat"):
    # Проверяем, является ли пользователь новым и нужно ли создавать приватный чат со staff
    if not request.user.is_staff:
        # Ищем уже существующий приватный чат между пользователем и любым staff
        chat_group = ChatGroup.objects.filter(
            is_private=True,
            users_in_chat=request.user,
            users_in_chat__in=User.objects.filter(is_staff=True)
        ).first()

        # Если чата нет, создаем новый с первым доступным staff пользователем
        if not chat_group:
            staff_user = User.objects.filter(is_staff=True).first()  # Берем первого staff пользователя
            if staff_user:
                # Генерируем уникальное имя чата
                group_name = f'private-{request.user.username}-{staff_user.username}-{get_random_string(8)}'
                
                chat_group = ChatGroup.objects.create(
                    group_name=group_name,
                    is_private=True,
                    other_user=staff_user
                )
                chat_group.users_in_chat.add(request.user, staff_user)

            return redirect('chat:chatroom', chatroom_name=chat_group.group_name)

    # Если пользователь уже в чате или является staff
    chat_group = get_object_or_404(ChatGroup, group_name=chatroom_name)
    
    # Загружаем последние 30 сообщений из текущего чата
    chat_messages = chat_group.chat_messages.all()[:30]
    
    # Загружаем список всех чатов для staff
    if request.user.is_staff:
        chat_list = ChatGroup.objects.filter(users_in_chat=request.user)
    else:
        chat_list = []

    # Проверка на запрос через htmx
    if request.htmx:
        form = ChatmessageCreateForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            context = {
                'message': message,
                'user': request.user
            }
            return render(request, 'chat/partials/chat_message_p.html', context)

    return render(request, 'chat/chat.html', {
        'chat_messages': chat_messages,  # Сообщения из текущего чата
        'form': ChatmessageCreateForm(),
        'chat_list': chat_list,  # Список чатов для staff
        'current_chatroom': chat_group  # Текущая комната
    })
