from django.urls import path
from . import views  #句点让 Python 从当前 urls.py 模块所在的文件夹中导入 views

app_name = 'learning_logs'
urlpatterns = [         
    # 主页
    path('', views.index, name='index'),
    path('topics/',views.topics,name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic')
]   
#     让 Django 查找在基础 URL 后紧跟单词 topics 的
# URL，第二部分（/<int:topic_id>/）与在两个斜杠之间的整
# 数匹配，并将这个整数赋给实参 topic_id。
    
#urlpatterns 是一个列表，包含可在应用程序 learning_logs中请求的网页
