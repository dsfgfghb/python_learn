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
    