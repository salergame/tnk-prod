from django.urls import path, reverse_lazy
from ps_account import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView


app_name='ps_account'

urlpatterns = [
    path('registration/', views.register, name='registration'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.account, name='account'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='change_password.html',
        success_url=reverse_lazy('user_account')  
    ), name='change_password'),
    path('change-email/', views.change_email, name='change_email'),
    path('delete-account/', views.delete_account, name='delete_account'),
]