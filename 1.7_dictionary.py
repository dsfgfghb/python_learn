print("----------------------------------------------------------------------------------------")
#6.1一个简单的字典
print("6.1一个简单的字典")
alien_0 = {'color':'green','point':5}

print(alien_0['color'])
print(alien_0['point'])

print("----------------------------------------------------------------------------------------")
#6.2.1访问字典的值
print("6.2.1访问字典的值")
alien_0 = {'color':'green','point':5}       #{}内为字典内容

print(alien_0['color'])             #访问字典时用 [] ,[] 内为键
new_point = alien_0['point']
print(f"You just earned {new_point} points!")

print("----------------------------------------------------------------------------------------")
#6.2.2添加键值对
print("6.2.2添加键值对")
alien_0 = {'color':'green','point':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25          #字典可以根据键直接修改该键的值,若没有该键则添加该键并赋值

print(alien_0)

print("----------------------------------------------------------------------------------------")
#6.2.3创建空字典
print("6.2.3创建空字典")
alien_0 = { }                           #一个{} 即可创建一个空字典

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

print("----------------------------------------------------------------------------------------")
#6.2.4修改字典的值
print("6.2.4修改字典的值")
alien_0 = {'color' : 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")
alien_0 = {'x_position':0,'y_position':25 ,'speed':'medium'}
print(f"Original positon : {alien_0['x_position']}")

if alien_0 ['speed'] == 'slow':     #
    x_increment =1
elif alien_0['speed'] =='medium':
    x_increment =2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position']+x_increment

print(f"Now positon: {alien_0['x_position']}")

print("----------------------------------------------------------------------------------------")
#6.2.5删除键
print("6.2.5删除键")
alien_0 = {'color':'green','point':5}
print(alien_0)
del alien_0['point']            #del 字典[键] 可以删除对应的键
print(alien_0)

print("----------------------------------------------------------------------------------------")
#6.2.6 由类似的对象组成的字典
print("6.2.6 由类似的对象组成的字典")
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',                 #能够储存多个信息
 }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

print("----------------------------------------------------------------------------------------")
#6.2.7 使用 get() 来访问值
print("6.2.7 使用 get() 来访问值")
alien_0 = {'color' : 'green','speed':'slow'}
# print(alien_0['points'])            #直接访问字典没有的键会报错
point_value = alien_0.get('points','No point value assigned.')      #字典.get(键,value)  会返回该键的值,若没有该键则返回value
print(point_value)
