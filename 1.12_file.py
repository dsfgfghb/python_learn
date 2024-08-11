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