print("----------------------------------------------------------------------------------------")
#7.1
car = input("What kind of car you want?")
print(f"Let me see if I can find you a {car}")

print("----------------------------------------------------------------------------------------")
#7.2
nomber = input("How many people have meat?")
nomber = int(nomber)
if nomber > 8:
    print("There didn't have enough free table")
else:
    print("There have some free table")
    
print("----------------------------------------------------------------------------------------")
#7.3
nomber = input("Please tell me a nomber")
nomber = int(nomber)
if nomber % 10 == 0:
    print("Yes!")
else:
    print("No!")

print("----------------------------------------------------------------------------------------")
#7.4
while True:
    pizza = input('Please tell what do you want')
    if pizza == 'quit':
        break
    else:
        print(f"{pizza} will be add to your pizza!")
        
print("----------------------------------------------------------------------------------------")
#7.5
while True:
    age= input("How old are yuo?")
    try:
        age =int(age)
    except:
        break
    if age <=3:
        print("you are free!")
    elif age <=12:
        print("you need to pay 10$.")
    else :
        print("you need to pay 15$.")

print("----------------------------------------------------------------------------------------")
#7.6
pizza = ''
while pizza != 'quit':
    pizza = input('Please tell what do you want')
    print(f"{pizza} will be add to your pizza!")

active =True
while active:
    pizza = input('Please tell what do you want')
    if pizza == 'quit':
        active = False
    else:
        print(f"{pizza} will be add to your pizza!")

while True:
    pizza = input('Please tell what do you want')
    if pizza == 'quit':
        break
    else:
        print(f"{pizza} will be add to your pizza!")

print("----------------------------------------------------------------------------------------")
#7.7
while 1:
    print("Unlimit time")