from django.urls import path
from . import views  #句点让 Python 从当前 urls.py 模块所在的文件夹中导入 views

app_name = 'learning_logs'
urlpatterns = [         
    # 主页
    path('', views.index, name='index'),
]       #urlpatterns 是一个列表，包含可在应用程序 learning_logs中请求的网页