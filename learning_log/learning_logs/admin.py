from django.contrib import admin

# Register your models here.

from .models import Topic   #前面的 . 是让Django在adimin.py这个文件查找models.py
from .models import Entry
admin.site.register(Topic)
admin.site.register(Entry)
