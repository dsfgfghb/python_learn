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

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:                            #转换成int类型之后可以进行数值比较
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
    
    
print("----------------------------------------------------------------------------------------")
#7.1.3 求模运算符 % 
print("7.1.3 求模运算符 % ")

#  %  为取余数

