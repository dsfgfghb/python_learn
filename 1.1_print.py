# print("hello world")

message="hello python world"
print(message)

message="Hello Python Crash Course world!"
print(message)
print("---------------------------------")

name = "ada lovelace"
print(name.title())  #首字母大写
print(name.upper())  #所有字母大写
print(name.lower())  #所有字母小写

print("---------------------------------")

# 用f""插入变量
first_name='ada'
last_name="lovelace"
full_name=f"{first_name} {last_name}" #插入变量
print(full_name)

print(f"hello,{full_name.title()}") 
message=f"hello,{full_name.title()}"
print(message)

print("----------------------------------")

# \t \n
print("Python")
print("\tpython")   #\t代表着一个制表符

print("languages:\nPython,\nc,\njavascript")   #\n代表着一个换行符
print("\n")
print("languages:\n\tPython,\n\tc,\n\tjavascript")   #\n\t的组合




