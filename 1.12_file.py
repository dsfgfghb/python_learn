print("----------------------------------------------------------------------------------------")
#10.1.1读取文件的全部内容 
print("10.1.1读取文件的全部内容")
from pathlib import Path
path = Path('python_learn/pi_digits.txt')      #创建了一个表示文件的Path对象
contents = path.read_text()                     #将文件内的所有内容付给contents
print(contents)

print("----------------------------------------------------------------------------------------")
#10.1.2相对路径和绝对路径 
print("10.1.2相对路径和绝对路径")

#相对路径 : 'python_learn/pi_digits.txt'
#绝对路径 : 'D:/vscode/python_learn/python_learn/pi_digits.txt'

print("----------------------------------------------------------------------------------------")
#10.1.3 访问文件中的各行 
print("10.1.3 访问文件中的各行")
lines = contents.splitlines()           #返回一个列表,其中包含文档的所有行
print(lines)
for line in lines:
    print(line)


print("----------------------------------------------------------------------------------------")
#10.1.4 使用文件的内容 
print("10.1.4 使用文件的内容")

pi_string = ''
for line in lines:
    pi_string+=line.lstrip()     #将文件里的文字存起来  因为原来每行的左边都有空格,用lstrip()去除

print(pi_string)
print(len(pi_string))

print("----------------------------------------------------------------------------------------")
#10.1.5 包含 100 万位的大型文件 
print("10.1.5 包含 100 万位的大型文件")

#可以像上面一样处理大型文件
#可处理的数据量方面，Python 没有任何限制。只要系统的内存足够大，你想处理多少数据就可以处理多少数据。

print("----------------------------------------------------------------------------------------")
#10.1.6 圆周率值中包含你的生日吗 
print("10.1.6 圆周率值中包含你的生日吗")

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits ofpi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

print("----------------------------------------------------------------------------------------")
#10.2.1 写入一行 
print("10.2.1 写入一行")
path = Path('programming.txt')              
path.write_text("I love programming.")      #write_text(string)会在文档中写入一行文字  python只能将字符串写入文件    

print("----------------------------------------------------------------------------------------")
#10.2.2 写入多行 
print("10.2.2 写入多行")

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
path.write_text(contents)               #使用write_text()时 如果指定文件已经存在,那么其原本的内容将会被删除





print("----------------------------------------------------------------------------------------")       #异常
#10.3.1 处理 ZeroDivisionError 异常 
print("10.3.1 处理 ZeroDivisionError 异常")
# print(5/0)                    #会报错

print("----------------------------------------------------------------------------------------")       
#10.3.2 使用 try-except 代码块 
print("10.3.2 使用 try-except 代码块")

try:
    print(5/0)      #若try代码块运行没有问题,Python会跳过except代码块
except ZeroDivisionError:
    print("You can't divide by zero!")      #若try代码块产生了问题,Python会查找指出了该怎么办的except代码块
                                            #并执行其中的代码

print("----------------------------------------------------------------------------------------")       
#10.3.3 使用异常避免崩溃 
print("10.3.3 使用异常避免崩溃")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     answer = int(first_number) / int(second_number)     #若用户输入0作为除数 程序会报错
#     print(answer)

print("----------------------------------------------------------------------------------------")       
#10.3.4 else 代码块 
print("10.3.4 else 代码块")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:

        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")     
    else:
        print(answer)

print("----------------------------------------------------------------------------------------")       
#10.3.5 处理 FileNotFoundError 异常 
print("10.3.5 处理 FileNotFoundError 异常")

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')         #指定读取的编码格式     没有该文件,报错  FileNotFoundError
except FileNotFoundError:
    print(f"sorry the file {path} does not exist.")


print("----------------------------------------------------------------------------------------")       
#10.3.6 分析文本 
print("10.3.6 分析文本")

path = Path('python_learn/alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    words = contents.split()                                #计算有多少个单词
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")


print("----------------------------------------------------------------------------------------")       
#10.3.7 使用多个文件 
print("10.3.7 使用多个文件")

def count_words(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        words = contents.split()                                
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

path = Path('python_learn/alice.txt')
count_words(path)

filenames =  ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']           #导入多个文件
for filename in filenames:
    path = Path(filename)
    count_words(path)

print("----------------------------------------------------------------------------------------")       
#10.3.8 静默失败 
print("10.3.8 静默失败")
#pass 语句可以让Python什么都不做
def count_words(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print(f"Sorry, the file {path} does not exist.")
        pass
    else:
        words = contents.split()                                
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")
    
print("----------------------------------------------------------------------------------------")       
#10.4.1使用 json.dumps() 和 json.loads() 
print("10.4.1使用 json.dumps() 和 json.loads()")

import json

numbers = [2,3,5,7,11,13]

path = Path('number.json')
contents = json.dumps(numbers)         #json.dumps()接受一个实参,然后将该实参转化成JSON的格式
path.write_text(contents)

contents = path.read_text()
numbers=0
numbers = json.loads(contents)          #json.lodes()将一个json格式的字符串作为参数,并返回一个Python对象
print(numbers)

print("----------------------------------------------------------------------------------------")       
#10.4.2 保存和读取用户生成的数据 
print("10.4.2 保存和读取用户生成的数据")

username = input("What is your name?")

path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)
print(f"We'll remember you when you come back,{username}")

contents = path.read_text()
username= json.loads(contents)
print(f"Welcome back,{username}")

if path.exists():                       #如果指定的文件存在 exists()函数会返回True ,否则返回false
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")

print("----------------------------------------------------------------------------------------")       
#10.4.3 重构 
print("10.4.3 重构")
def greet_user():
    path = Path('username.json')
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back,{username}!")
greet_user()

def get_stored_username(path):
    if path.exists():  
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
def greet_user():                   #重构了该函数
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back,{username}!")

greet_user()

