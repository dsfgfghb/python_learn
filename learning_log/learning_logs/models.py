from django.db import models

# Create your models here.
class Topic(models.Model):              # 一个继承了model的类
    text = models.CharField(max_length=200)     # CharField是字符串字段   max_length=200代表预留了多少空间(即200个字符)
    #需要存储少量文本（如名称、标题或城市）时,可使用CharField。
    date_added = models.DateTimeField(auto_now_add=True)
    #DateTimeField 是一个记录时间的数据  auto_now_add=True 表示自动设置当前时间

    def __str__(self):   #如果模型有__str__()方法,那么每次需要生成表示模型实例的输出时,都会调用这个方法
        return self.text