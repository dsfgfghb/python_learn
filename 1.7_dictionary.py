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

print("----------------------------------------------------------------------------------------")
#6.3.1遍历所有的键值对
print("6.3.1遍历所有的键值对")
user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi'
}
for key,value in user_0.items():           #声明两个变量来获得所有的信息
    print(f"\nkey:{key}")
    print(f"Value:{value} ")

print("----------------------------------------------------------------------------------------")
#6.3.1遍历所有的键
print("6.3.1遍历所有的键")
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',                
 }

for name in favorite_languages.keys():          #.keys() 会提取字典里所有的键
    print(name.title())


for name in favorite_languages:          #在遍历字典时会默认遍历所有的键,所以不加.keys()时输出不变
    print(name.title())
    
print("----------------------------------------------------------------------------------------")
#6.3.3 按特定的顺序遍历字典中的所有键
print("6.3.3 按特定的顺序遍历字典中的所有键")
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',                
 }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()},thank you for taking our poll!")         #sorted() 会给字典排序

print("----------------------------------------------------------------------------------------")
#6.3.4 遍历字典中的所有值
print("6.3.4 遍历字典中的所有值")
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',                
 }

print("The following languages have been mentioned:")           
for language in favorite_languages.values():                    #.values() 会提取所有的值
    print(language.title())
    
print("----------------------------------------------------------------------------------------")
#6.4.1字典列表
print("6.4.1字典列表")
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0,alien_1,alien_2]              #用列表储存多个字典

for alien in aliens:
    print(alien)
    
aliens = []
for alilen_nomber in range (30):
    new_alien = {'color': 'green', 'points': 5,'speed' : 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")

print(f"Total number of aliens:{len(aliens)}!")

print("----------------------------------------------------------------------------------------")
#6.4.2在字典中存储列表
print("6.4.2在字典中存储列表")
pizza = {
    'crust' : 'thick',
    'toppints' : ['mushroom','extra cheese']            #用字典存储列表
}

print(f"You ordered a {pizza['crust']}-crust pizza"
      "with the following toppings:")

for topping in pizza['toppints']:               #读取字典中的列表
    print (f"\t{topping}")

favorite_languages = {
 'jen': ['python','rust'],
 'sarah': ['c'],
 'edward': ['rust','go'],
 'phil': ['python','haskell'],                
 }

for name , languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language:")
    for language in languages:
        print(f"\t{language.title()}")

print("----------------------------------------------------------------------------------------")
#6.4.3 在字典中存储字典
print("6.4.3 在字典中存储字典")

users = {
    'aeinstein' : {
        'first' :'albert',
        'last' : 'einstein',
        'location'  : 'princeton',
    },
    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris',
    },
}
for username,user_info in users.items():
    print(f"\tUsername:{username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location}")