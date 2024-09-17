from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.urls import reverse
from ps_account.forms import RegisterForm
from .forms import EmailChangeForm


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