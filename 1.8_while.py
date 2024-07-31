print("----------------------------------------------------------------------------------------")
#7.1 input()函数的工作原理
print("7.1 input()函数的工作原理")
#message = input("Tell me something, and I wil repeat it back to you:")      #input('提示')内的参数为给用户的提示,程序会在这等待用户输入
#print(message)                                                              #用户按回车键后继续运行程序并返回用户输入的数据

print("----------------------------------------------------------------------------------------")
#7.1.1编写清晰的提示
print("7.1.1编写清晰的提示")
# name = input ("Please enter your name:")
# print(f"\nHello,{name}!")

prompt = "If you share your name,we can personalize the messages you see."
prompt += "\nWhat is yur first name?"                                   #可以将提示赋给一个变量,再将变量给input()来实现多行的提示
# name= input(prompt)

print("----------------------------------------------------------------------------------------")
#7.1.2 使用 int() 来获取数值输入
print("7.1.2 使用 int() 来获取数值输入")

# age = input("How old are you?")                 #用input()时返回的是字符串 不可以用于数值比较 age >18等操作

# age  = int(age)                     #将字符串转化成int类型

# height = input("How tall are you, in inches? ")
# height = int(height)
# if height >= 48:                            #转换成int类型之后可以进行数值比较
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")
    
    
print("----------------------------------------------------------------------------------------")
#7.1.3 求模运算符 % 
print("7.1.3 求模运算符 % ")

#  %  为取余数


print("----------------------------------------------------------------------------------------")
#7.2.1 使用 while 循环
print("7.2.1 使用 while 循环")
current_nomber = 1
while current_nomber <=5:           #while 只要条件满足,就会重复执行后面的语句
    print(current_nomber)
    current_nomber += 1
    
print("----------------------------------------------------------------------------------------")
#7.2.2 让用户选择何时退出
print("7.2.2 让用户选择何时退出")

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ''
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

print("----------------------------------------------------------------------------------------")
#7.2.3使用标志
print("7.2.3使用标志")
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True                       #将active作为结束的标志 
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

print("----------------------------------------------------------------------------------------")
#7.2.使用break退出循环
print("7.2.4使用break退出循环")
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
        
print("----------------------------------------------------------------------------------------")
#7.2.5 在循环中使用 continue
print("7.2.5 在循环中使用 continue")
current_nomber = 0
while current_nomber < 10:
    current_nomber +=1
    if current_nomber % 2==0:   
        continue                            #当执行continue时程序会立即退出该循环,并进行下一次的循环,continue后面的语句将不会被执行
    print(current_nomber)
    
print("----------------------------------------------------------------------------------------")
#7.2.6 避免无限循环
print("7.2.6 避免无限循环")
x = 1
while x<=5:
    print(x)                                 #当程序被写成了无限循环时,可以按下ctrl+c键退出程序