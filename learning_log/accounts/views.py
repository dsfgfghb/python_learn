from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    if request.method !='POST':
        form = UserCreationForm()# 显示空的注册表单
    else :
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)# 让用户自动登录，再重定向到主页
            return redirect('learning_logs:index')
    context = {'form':form}# 显示空表单或指出表单无效
    return render(request, 'registration/register.html', context)
    