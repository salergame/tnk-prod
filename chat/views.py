from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required
from .models import ChatGroup, GroupMessage
from .forms import ChatmessageCreateForm

@login_required
def chat_views(request, chatroom_name="public-chat"):
    # Получаем текущую группу чата
    chat_group = get_object_or_404(ChatGroup, group_name=chatroom_name)
    
    # Загружаем последние 30 сообщений из текущего чата
    chat_messages = chat_group.chat_messages.all()[:30]
    
    # Загружаем список всех чатов для staff
    if request.user.is_staff:
        chat_list = ChatGroup.objects.filter(users_online=request.user)  # Убедись, что фильтр правильный
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
