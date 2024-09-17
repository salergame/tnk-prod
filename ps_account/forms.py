from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Этот email уже используется.')
        return email

from django import forms
from django.core.validators import EmailValidator


class EmailChangeForm(forms.Form):
    new_email = forms.EmailField(
        label='Новый Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        validators=[EmailValidator()],
        help_text='Введите ваш новый email'
    )