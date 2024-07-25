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
