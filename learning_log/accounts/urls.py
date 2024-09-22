from django.urls import path,include
from . import views

app_name = 'accounts'
urlpatterns = [
    path('',include('django.contrib.auth.urls')), #include('django.contrib.auth.urls')用于引入 Django 自带的身份认证系统中的 URL 配置
    path('register/', views.register, name='register'),
]