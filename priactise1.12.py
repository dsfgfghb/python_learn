print("----------------------------------------------------------------------------------------")
#10.3
from pathlib import Path as Pa

from pathlib import Path
path = Pa('python_learn/pi_digits.txt')      
contents = path.read_text() 
string=''                    
for line in contents.splitlines():
    string+=line.lstrip()
print(string)

print("----------------------------------------------------------------------------------------")
#10.4
name = input("Please tell me your name:")+'\n'
path = Pa('guest.txt')
path.write_text(name)

print("----------------------------------------------------------------------------------------")
#10.5
while True:
    temp=input("name:")
    if temp == 'q':
        break
    name+=temp+'\n'
path.write_text(name)
    
print("----------------------------------------------------------------------------------------")
#10.6
print('Tell me 2 nomber')
a=input()
b=input()
try:
    a=int(a)+int(b)
except ValueError:
    pass
else:
    print(a)

print("----------------------------------------------------------------------------------------")
#10.7
while True:
    a=input()
    if a=='q':
        break
    b=input()
    if b=='q':
        break
    try:
        a=int(a)+int(b)
    except ValueError:
        pass
    else:
        print(a)

print("----------------------------------------------------------------------------------------")
#10.8

cats=Pa('python_learn/cats.txt')
dogs=Pa('python_learn\dogs.txt')
files = [cats,dogs]
for file in files:
    try:
        contents = file.read_text(encoding='UTF-8')
    except:
        # print(f"Sorry, the file {path} does not exist.")
        pass
    else:
        lines=contents.splitlines()
        for line in lines:
            print(f"your dog/cat name is {line}")

