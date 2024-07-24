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

