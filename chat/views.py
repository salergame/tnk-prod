from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import ChatGroup
from .forms import ChatmessageCreateForm

@login_required
def chat_views(request, chatroom_name=None):
    # Функционал поиска
    search_query = request.GET.get('search', '')

    # Проверяем, если у пользователя нет чатов
    if not ChatGroup.objects.filter(users_in_chat=request.user).exists():
        # Если нет чатов, находим любого пользователя со статусом staff
        staff_user = User.objects.filter(is_staff=True).first()

        if staff_user:
            # Создаем новый чат с staff пользователем
            new_chat = ChatGroup.objects.create(group_name=f"private-{request.user.username}-{staff_user.username}")
            new_chat.users_in_chat.add(request.user, staff_user)

            # Перенаправляем пользователя в новый созданный чат
            return redirect('chat:chatroom', chatroom_name=new_chat.group_name)
        else:
            # Если нет staff пользователей, перенаправляем на главную
            return redirect('main:index')

    # Если chatroom_name не передан, проверяем, является ли пользователь staff
    if not chatroom_name:
        if request.user.is_staff:
            # Если это staff пользователь, показываем список чатов с возможным поиском
            if search_query:
                # Фильтруем чаты по названию
                chat_list = ChatGroup.objects.filter(group_name__icontains=search_query, users_in_chat=request.user).distinct()
            else:
                # Если поиска нет, показываем все чаты, где есть пользователь
                chat_list = ChatGroup.objects.filter(users_in_chat=request.user)
            first_chat = chat_list.first()
            if first_chat:
                return redirect('chat:chatroom', chatroom_name=first_chat.group_name)
            else:
                return redirect('main:index')  # Если чатов нет
        else:
            return redirect('main:index')  # Если не staff, перенаправляем на главную

    # Если пользователь уже в чате или является staff
    chat_group = get_object_or_404(ChatGroup, group_name=chatroom_name)

    # Загружаем последние 30 сообщений из текущего чата
    chat_messages = chat_group.chat_messages.all()[:30]

    # Загружаем список всех чатов для staff с фильтрацией по названию
    if request.user.is_staff:
        if search_query:
            # Фильтруем чаты по названию чата
            chat_list = ChatGroup.objects.filter(group_name__icontains=search_query, users_in_chat=request.user).distinct()
        else:
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
        'chat_messages': chat_messages,
        'form': ChatmessageCreateForm(),
        'chat_list': chat_list,  # Список чатов для staff, с фильтрацией по названию чата
        'current_chatroom': chat_group  # Текущая комната
    })
