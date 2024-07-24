magicians = ['alice', 'david', 'carolina']
for magician in magicians:                  #for循环遍历magicians里的元素,会反复将magicians里的元素赋给magician
    print(magician)                         #直到magicians里所有元素都被遍历完
    
for magician in magicians:                 
    print(magician.title() + ", that was a great trick!") 
    print(f"i can't wait to see your next trick,{magician.title()}.\n")
print("Thank you everyone, that was a great magic show!")
print("----------------------------------------------------------------------------------------")

for magician in magicians:      #  ":"不可以少会报错
#print(magician)             #后面的要循环的代码要缩进
    print(magician)
print(magician.title())           #该行代码没缩进,magician的值为最后一个元素的值

    #print(magician)            #一般情况下不能缩进
    
print("----------------------------------------------------------------------------------------")

for value in range(1,5):      # range(1,5)表示1到4的数字,左闭右开
    print(value)

nombers = list(range(1,6))    #可以用 list(range())生成一个列表
print(nombers)

nombers = list(range(2,11,2))       #range(2,11,2)表示从2开始,每次增加2,直到数字恰好不大于11 第一和第二个参数是范围,第三个参数是步长
print(nombers)

print("----------------------------------------------------------------------------------------")

squares = []
for value in range(1,11):
    squares.append(value**2)   #使用range来创建列表
print(squares)
print("----------------------------------------------------------------------------------------")
#4.4.1切片
print("4.4.1切片")
players = ['charles','martina','michael','florence','eli']
print(players[0:3])  #打印一个player列表的切片，该切片包含player前三名成员0,1,2  0为开始的成员的索引，3为最后的成员是该索引的前一个成员，即索引2对应的成员
print(players[1:4])
print(players[:4])   #若没有第一个索引，则从第一个开始
print(players[2:])   #若没有最后一个索引，则直到最后一个才结束
print(players[-3:])  #输出最后三个
print("----------------------------------------------------------------------------------------")
#4.4.2遍历切片
print("4.4.2遍历切片")
players = ['charles','martina','michael','florence','eli']
for player in players[:3]:
    print(player.title())
print("----------------------------------------------------------------------------------------")
# 4.4.3复制列表
print('4.4.3复制列表')
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]     #复制列表
# friend_foods = my_foods       #friend_foods和my_foods指向同一个列表，不是生成两个列表  (似乎是两个指向同一个地址的变量??)
my_foods.append("cannoli")

friend_foods.append("ice cream")        #可以确定确实有两个列表
print("My favorite foods are:")

print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)
print("----------------------------------------------------------------------------------------")
# 4.5.1元组
print("4.5.1定义元组")
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0]=250       #报错，元组元素不能被修改
my_t=(3,)       #严格地说，元组是由逗号标识的，圆括号只是让元组看起来更整洁、更清晰。
my_t=3,5,6
print(my_t)
print("----------------------------------------------------------------------------------------")
# 4.5.2遍历元组
print("4.5.1遍历元组")
dimensions=(200,50)
print("Original dimensions")
for dimension in dimensions:
    print(dimension)        #遍历元组内的元素

dimensions=(400,100)    #修改元组变量
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)