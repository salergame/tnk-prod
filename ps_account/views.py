from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.urls import reverse
from ps_account.forms import RegisterForm

# Create your views here.
def account(request):
    return render(request, 'ps_account/sit2.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('main:index'))
    else:
        form = RegisterForm()
        
    context = {
        'form': form
    }
    return render(request, 'ps_account/registration.html', context)