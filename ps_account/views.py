from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.urls import reverse
from ps_account.forms import RegisterForm
from .forms import EmailChangeForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def account(request):
    user = request.user
    context = {
        'user_name': user.get_full_name(),  # или user.username
        'user_email': user.email,
        'registration_date': user.date_joined.strftime('%d %B %Y')  # Форматируйте по вашему желанию
    }
    return render(request, 'ps_account/sit2.html', context)
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Explicitly authenticate the user with backend argument
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            if user is not None:
                auth_login(request, user)
                return redirect(reverse('main:index'))
    else:
        form = RegisterForm()
    
    context = {
        'form': form
    }
    return render(request, 'ps_account/registration.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect(reverse('ps_account:account'))
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'ps_account/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        return redirect('main:index')
    return render(request, 'ps_account/delete_account.html')

@login_required
def change_email(request):
    if request.method == 'POST':
        form = EmailChangeForm(request.POST)
        if form.is_valid():
            new_email = form.cleaned_data['new_email']
            user = request.user
            user.email = new_email
            user.save()
            messages.success(request, 'Ваш email был успешно изменен!')
            return redirect('user_account')
    else:
        form = EmailChangeForm()

    return render(request, 'ps_account/change_email.html', {'form': form})

def google_redirect(request):
    google_login_url = reverse('socialaccount_login', kwargs={'provider': 'google'})
    return redirect(google_login_url)

@login_required
def start_chat(request):
    """Пользователь начинает новый чат с сотрудником"""
    # Предположим, что сотрудник выбирается автоматически (первый доступный)
    staff_member = User.objects.filter(is_staff=True).first()

    # Проверяем, существует ли уже чат между пользователем и сотрудником
    chat_room, created = ChatRoom.objects.get_or_create(user=request.user, staff=staff_member)

    # Перенаправляем пользователя в комнату чата
    return redirect('chat_room', room_id=chat_room.id)


@login_required
def chat_room(request, room_id):
    """Показываем комнату чата и сообщения"""
    chat_room = get_object_or_404(ChatRoom, id=room_id)
    messages = chat_room.messages.all().order_by('timestamp')

    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            ChatMessage.objects.create(chat_room=chat_room, sender=request.user, message=message)
    
    return render(request, 'chat_room.html', {'chat_room': chat_room, 'messages': messages})


@login_required
def staff_chat_list(request):
    """Список всех чатов для сотрудника"""
    chat_rooms = ChatRoom.objects.filter(staff=request.user).order_by('-created_at')
    return render(request, 'staff_chat_list.html', {'chat_rooms': chat_rooms})