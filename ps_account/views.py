from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.urls import reverse
from ps_account.forms import RegisterForm
from .forms import AvatarChangeForm, EmailChangeForm,DocumentUploadForm
from .models import UserDocument, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.
@login_required
def account(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)
    documents = UserDocument.objects.filter(user=user)

    if request.method == 'POST':
        avatar_form = AvatarChangeForm(request.POST, request.FILES, instance=profile)  # Важно передать request.FILES
        if avatar_form.is_valid():
            avatar_form.save()  # Сохраняем форму с загруженным файлом
            return redirect('ps_account:account')  # Перенаправляем после успешного сохранения
        else:
            print(avatar_form.errors)  # Вывод ошибок для отладки
    else:
        avatar_form = AvatarChangeForm(instance=profile)

    context = {
        'user_name': user.get_full_name() or user.username,
        'user_email': user.email,
        'registration_date': user.date_joined.strftime('%d %B %Y'),
        'documents': documents,
        'avatar_form': avatar_form,
        'avatar_url': profile.avatar.url if profile.avatar else '/media/avatars/baseavatar.jpg'  # Корректный путь к аватарке
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
            return redirect('ps_account:account')
    else:
        form = EmailChangeForm()

    return render(request, 'ps_account/change_email.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Чтобы избежать выхода пользователя из сессии
            return redirect('ps_account:account')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'ps_account/change_password.html', {'form': form})
def staff_check(user):
    return user.is_staff

@user_passes_test(staff_check)
@login_required
def staff_documents(request):
    query = request.GET.get('q', '')  # По умолчанию пустая строка, если ничего не передано
    if query:
        # Поиск по имени или email
        users = User.objects.filter(Q(username__icontains=query) | Q(email__icontains=query))
    else:
        # Вывод всех пользователей, если поисковый запрос не задан
        users = User.objects.filter(is_staff=False)
    
    return render(request, 'ps_account/staff_documents.html', {'users': users, 'query': query})


@user_passes_test(staff_check)
@login_required
def user_account_for_staff(request, user_id):
    # Get the user whose account staff want to manage
    selected_user = get_object_or_404(User, id=user_id)
    documents = UserDocument.objects.filter(user=selected_user)
    
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.user = selected_user
            document.save()
            return redirect('ps_account:user_account_for_staff', user_id=user_id)
    else:
        form = DocumentUploadForm()

    context = {
        'user_name': selected_user.get_full_name(),
        'user_email': selected_user.email,
        'registration_date': selected_user.date_joined.strftime('%d %B %Y'),
        'documents': documents,
        'form': form,  # For document upload
    }
    return render(request, 'ps_account/sit2.html', context)


@user_passes_test(staff_check)
@login_required
def delete_document(request, user_id, document_id):
    document = get_object_or_404(UserDocument, id=document_id, user_id=user_id)
    document.delete()
    return redirect('ps_account:user_account_for_staff', user_id=user_id)