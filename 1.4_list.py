bicycles = ['trek', 'cannondale', 'redline', 'specialized']     #列表
print(bicycles)     #会直接打印出列表: ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])       #会打印出列表中的第一个元素: trek  索引从0开始
print(bicycles[0].title())    #可以直接调用字符串方法

print(bicycles[-1])       #会打印出列表中的最后一个元素: specialized

message=f"My first bicycle was a {bicycles[0].title()}."
print(message)

bicycles[0]='ducati'    #可以直接修改列表中的元素
print(bicycles)

bicycles.append('honda')    #  append("元素") 可以直接在列表末尾添加元素
print(bicycles)

bicycles.insert(1,'yamaha')     # insert(位置,"要插入的元素") 可以在列表中任意位置插入元素,该位置原本的元素以及后面的元素会全部先后移动一位
print(bicycles)

del bicycles[0]       #del 列表名[索引] 可以直接删除列表中的元素
print(bicycles)

motorcycle=bicycles.pop()     #  pop()  可以直接删除列表末尾的元素，并返回被删除的元素 "相当于弹出栈顶元素"
print(motorcycle)
print(bicycles)         # 末尾的元素已将被删除
motorcycle=bicycles.pop(1)     #  pop(索引) 可以直接删除对应索引的元素,并返回被删除的元素
print(motorcycle)
 
bicycles=['trek', 'cannondale', 'redline', 'specialized'] 

bicycles.remove('trek')     # remove("元素") 可以直接删除列表中第一个出现的该元素，如果该元素不存在，会报错