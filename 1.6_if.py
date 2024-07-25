#5.1 if语句实例
print("5.1 if语句实例")
cars = ["audi",'bmw','subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())
print("----------------------------------------------------------------------------------------")
#5.2.1检查是否相等
print("5.2.1检查是否相等")
car = 'bmw'        
car =='bmw'         #True
print(car =='bmw')
car =="audi"        #False
print(car =="audi" )
print("----------------------------------------------------------------------------------------")
#5.2.2检查时忽略大小写
print("5.2.2检查时忽略大小写")
car = "Audi"
car == 'audi'
print(car == 'audi')       #False
car.lower() =='audi'
print(car.lower() =='audi')    #True
print(car)  #不影响变量
print("----------------------------------------------------------------------------------------")
#5.2.3检查是否不等
print("5.2.3检查是否不等")
requested_topping='mushrooms'
if requested_topping !='anchovies':
    print("Hold the anchovies!")
print("----------------------------------------------------------------------------------------")
#5.2.4数值比较
print("5.2.4数值比较")
age=18
print(age==18 )    #True  比较两个数是否不等
answer=17
if answer !=42:
    print("That is not the correct answer.Please try angin!")
age = 19
print(age<21)       #数学比较
print("----------------------------------------------------------------------------------------")
#5.2.5检查多个条件
print("5.2.5检查多个条件")
age_0=22
age_1=18
print(age_0>=21 and age_1>=21)      #False  and：左右两个的值都为True时返回True
age_1=22
print(age_0>=21 and age_1>=21)      #True
print((age_0>=21) and (age_1>=21))   #改善可读性

age_0=22
age_1=18
print(age_0>=21 or age_1>=21)       #True   or:  左右两个只要有一个为True就返回True
age_0=18
print(age_0>=21 or age_1>=21)       #False
print("----------------------------------------------------------------------------------------")
#5.2.6检查特定的值是否在列表中
print("5.2.6检查特定的值是否在列表中")
requested_topping=['mushrooms','onions','pineapple']
print('mushrooms'in requested_topping)          #True  用in判断是否在列表中 若在则返回True，反之返回False
print('pepperoni'in requested_topping)          #False
print("----------------------------------------------------------------------------------------")
#5.2.7检查特定的值是否不在列表中
print("5.2.7检查特定的值是否不在列表中")
bannes_users = ['andrew','carolina','david']
user = 'marie'
if user not in bannes_users:
    print(f"{user.title()},you can post a response if you wish.")       #用not in 可以判断一个值是否在列表中 若不在则返回True，反之返回False
print("----------------------------------------------------------------------------------------")
#5.2.8；布尔表达式
game_active= True       
can_edit = False        #布尔表达式的结果要么为True，要么为False
print("----------------------------------------------------------------------------------------")
#5.3.1简单的if语句
print("5.3.1简单的if语句")
#if conditional_test:
#   do something
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
print("----------------------------------------------------------------------------------------")
#5.3.2if-else语句
print("5.3.2if-else语句")
age = 17
if age >= 18:
    print("you are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry,you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
    
print("----------------------------------------------------------------------------------------")
#5.3.3if-elif-else语句
print("5.3.3if-elif-else语句")
age=12
if age <4:
    print("Your admission cost is $0.")
elif age < 18:
    print("your admission const is $25.")
else :
    print("your admission cost is $40.")
#简化
if age < 4:
    price = 0
elif age <18 :
    price = 25
else :
    price = 40
print(f"your admission const is ${price}.")

print("----------------------------------------------------------------------------------------")
#5.3.4使用多个elif代码块
print("5.3.4使用多个elif代码块")
age = 12
if age <4:
    price = 0
elif age <18:
    price = 25
elif age <65:
    price = 40
else: 
    price = 20
print(f"your admission const is ${price}.")

print("----------------------------------------------------------------------------------------")
#5.3.5省略else代码块
print("5.3.5省略else代码块")
#最后的else可以省略
age = 12
if age <4:
    price = 0
elif age <18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"your admission const is ${price}.")

print("----------------------------------------------------------------------------------------")
#5.3.6测试多个条件
print("5.3.6测试多个条件")
requested_toppings = ['mushrooms','extra cheese']
if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:       #不能用elif,因为只要有一个条件通过,就会跳过余下的条件测试
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
print("\nFinished making your pizza!")
