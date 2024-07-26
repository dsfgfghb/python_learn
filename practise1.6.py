#5.1
nomber1=190**2
print("Is nomber1 == 36100? I guess it is True.")
print(nomber1==36100)
nomber2=3.11
print("Is nomber2 > 3.8? I guess it is False")
print(3.11>3.8)
nomber3=0.8*0.5
print("Is nomber3 == 0.4? I guess it is True")
print(nomber3==0.4)
nomber4=365-1
print("Is nomber4 == 366? I guess it is False")
print(nomber4==366)
nomber5 = 3.14
print("Is nomber5 >3.13? I guess it is True")
print(nomber5>3.13)
print("----------------------------------------------------------------------------------------")
#5.2
first_string='Apple'
second_string='banana'
print(first_string==second_string)
print(second_string=='banana')
print(first_string.lower()=='apple')
print(3.14*3>99)
print(-0.01>0 and 1<1)
print(1>0 or -1>0)
TheList=['car','cat','cattle']
print('dog' in TheList)
print('dog' not in TheList)

print("----------------------------------------------------------------------------------------")
#5.3
alien_color='green'
if alien_color == 'green':
    print("you get 5 score!")
alien_color = 'red'
if alien_color == 'green':
    print("you get 5 score!")
print("----------------------------------------------------------------------------------------")
#5.4
alien_color = 'green'
if alien_color == 'green':
    print("you distory a green alien and get 5 score.")
else:
    print("you destory a alien which is not green and get 10 score.")
alien_color = 'red'
if alien_color == 'green':
    print("you distory a green alien and get 5 score.")
else:
    print("you destory a alien which is not green and get 10 score.")
    
print("----------------------------------------------------------------------------------------")
#5.5
alien_color = 'green'
if alien_color == 'green':
    print("you distory a green alien and get 5 score.")
elif alien_color == 'yellow':
    print("you destory a yellow alien and get 10 score.")
elif alien_color == 'red':
    print("you destory a red alien and get 15 score.")
    
alien_color = 'yellow'
if alien_color == 'green':
    print("you distory a green alien and get 5 score.")
elif alien_color == 'yellow':
    print("you destory a yellow alien and get 10 score.")
elif alien_color == 'red':
    print("you destory a red alien and get 15 score.")
    
alien_color = 'red'
if alien_color == 'green':
    print("you distory a green alien and get 5 score.")
elif alien_color == 'yellow':
    print("you destory a yellow alien and get 10 score.")
elif alien_color == 'red':
    print("you destory a red alien and get 15 score.")
    
print("----------------------------------------------------------------------------------------")
#5.6
age = 1
if age <2:
    print("It is a baby.")
elif age < 4:
    print("It is a child.")
elif age <13:
    print("It is a childen.")
elif age <18:
    print("It is a teenager.")
elif age < 65:
    print("It is a middle-aged people.")
elif age >= 65:
    print("It is a elder.")
print("----------------------------------------------------------------------------------------")
#5.7
favorite_fruits=['apple','banana','watermelon']
if 'apple' in favorite_fruits:
    print("You really like apple!")
if 'banana' in favorite_fruits:
    print("You really like banana!")
if 'watermelon' in favorite_fruits:
    print("You really like watermelon!")
print("----------------------------------------------------------------------------------------")
#5.8
namelist = ['tom','jerry','tome','admin','jeson']
for item in namelist:
    if item == 'admin':
        print(f"Hello {item},would you like to see a status report?")
    else :
        print(f"Hello {item},thank you for logging in again.")
print("----------------------------------------------------------------------------------------")
#5.9
namelist = []

if namelist :
    for item in namelist:
        if item == 'admin':
            print(f"Hello {item},would you like to see a status report?")
        else:
            print(f"Hello {item},thank you for logging in again.") 
else :
       print("We need to find some users!")
print("----------------------------------------------------------------------------------------")
#5.10
current_users = ['Tom','Jerry','tome','admin','adc']
new_users = ['Tom','QQ','Tab','Jerry','enter']
current_users_lower = current_users[:]

for i in range(0,len(current_users_lower)):
    current_users_lower[i]=current_users_lower[i].lower()
    
for name in new_users:
    if name.lower() in current_users_lower:
        print(f"{name.capitalize()} has been used.you need to change your name.")
    else:
        print(f"{name.capitalize()} is not used")

print("----------------------------------------------------------------------------------------")
#5.11
nomber_list = []
for i in range(1,10):
    nomber_list.append(i)

for nomber in nomber_list:
    if nomber==1:
        print("1st")
    elif nomber ==2 :
        print('2nd')
    elif nomber == 3 :
        print("3rd")
    else :
        print(f"{nomber}th")