from django.urls import path
from ps_account import views

app_name='ps_account'

urlpatterns = [
    path('',views.account,name='account'),
    path('registration/',views.register,name='registration'),
]