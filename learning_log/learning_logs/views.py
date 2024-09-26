from django.shortcuts import render,redirect
from .models import Topic,Entry
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import TopicForm,EntryForm

# Create your views here.
def index(request):
    return render(request,'learning_logs/index.html')

@login_required #login_required() 的代码检查用户是否已登录。仅当用户已登录时，Django 才运行 topics() 的代码。否则重定向到登陆页面
def topics(request):
    # topics = Topic.objects.order_by('date_added')
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')#让 Django 只从数据库中获取 owner 属性为当前用户的 Topic 对象。
    
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request,topic_id):
    topic = Topic.objects.get(id=topic_id)

    if topic.owner != request.user:
        raise Http404
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic,'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()          #如果为GET 请求，创建一个新表单
    else:
        form = TopicForm(data = request.POST)
        if form.is_valid():#方法 is_valid() 核实用户填写了所有必不可少的字段
            
            new_topic = form.save(commit=False) #commit=False 允许你在保存前修改字段值。
            new_topic.owner = request.user  #将新主题的owner 属性设置为当前用户
            new_topic.save()
            
            # form.save()#调用save()，将表单中的数据写入数据库
            return redirect('learning_logs:topics')#使用 redirect()将用户的浏览器重定向到页面 topics
    
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
        print("id")
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic',topic_id=topic_id)
    context = {'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
    print("edit_entry")
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic
    
    if topic.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        form = EntryForm(instance=entry)#使用实参 instance=entry 创建一个EntryForm 实例
    else:
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic',topic_id=topic.id)
    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)
