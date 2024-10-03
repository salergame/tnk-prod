from django.urls import path, reverse_lazy
from ps_account import views
from django.conf import settings
from django.conf.urls.static import static

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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)