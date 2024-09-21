from django.shortcuts import render,redirect
from .models import Topic,Entry
from .forms import TopicForm,EntryForm

# Create your views here.
def index(request):
    return render(request,'learning_logs/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic,'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()          #如果为GET 请求，创建一个新表单
    else:
        form = TopicForm(data = request.POST)
        if form.is_valid():#方法 is_valid() 核实用户填写了所有必不可少的字段
            form.save()#调用save()，将表单中的数据写入数据库
            return redirect('learning_logs:topics')#使用 redirect()将用户的浏览器重定向到页面 topics
    
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)

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

def edit_entry(request,entry_id):
    print("edit_entry")
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic
    if request.method != 'POST':
        form = EntryForm(instance=entry)#使用实参 instance=entry 创建一个EntryForm 实例
    else:
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic',topic_id=topic.id)
    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)
