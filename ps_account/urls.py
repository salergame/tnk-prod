from django.urls import path, reverse_lazy
from ps_account import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name='ps_account'

urlpatterns = [
    path('registration/', views.register, name='registration'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.account, name='account'),
    path('change-password/', views.change_password, name='change_password'),
    path('change-email/', views.change_email, name='change_email'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('staff-documents/', views.staff_documents, name='staff_documents'),
    path('staff-documents/<int:user_id>/', views.user_account_for_staff, name='user_account_for_staff'),
    path('staff-documents/<int:user_id>/delete-document/<int:document_id>/', views.delete_document, name='delete_document'),
    
    # URL для сброса пароля
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='ps_account/password_reset_form.html',
             success_url=reverse_lazy('ps_account:password_reset_done'),
             email_template_name='ps_account/password_reset_email.html',
             subject_template_name='ps_account/password_reset_subject.txt',
         ), 
         name='password_reset'),
    
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='ps_account/password_reset_done.html'
         ), 
         name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='ps_account/password_reset_confirm.html',
             success_url=reverse_lazy('ps_account:password_reset_complete'),
         ), 
         name='password_reset_confirm'),
    
    path('password-reset-complete/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='ps_account/password_reset_complete.html'
         ), 
         name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)