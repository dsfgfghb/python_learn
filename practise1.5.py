#练习4.3
for i in range(1,21):
    print(i)

print("----------------------------------------------------------------------------------------")
#4.4
nomberList=[]
for i in range(1,1000001):
    nomberList.append(i)
print( min(nomberList))
print(max(nomberList))

print("----------------------------------------------------------------------------------------")
#4.5
nomberList=[]
for i in range(1,1000001):
    nomberList.append(i)
print( min(nomberList))
print(max(nomberList))
print( sum(nomberList))
print("----------------------------------------------------------------------------------------")
#4.6
nomberList=[]
for i in range(1,20,2):
    nomberList.append(i)
for i in nomberList:
    print(i)
print("----------------------------------------------------------------------------------------")
#4.7
nomberList=[]
for i in range(3,31):
    if(i%3==0):
        nomberList.append(i)
for i in nomberList:
    print(i)
print("----------------------------------------------------------------------------------------")
#4.8
nomberList=[]
for i in range(1,11):
    nomberList.append(i**3)
for i in nomberList:
    print(i)
print("----------------------------------------------------------------------------------------")
#4.9
nomberList=[]
for i in range(1,11):
    nomberList.append(i**3)
print("----------------------------------------------------------------------------------------")
#4.10
players = ['charles','martina','michael','florence','eli']
print(f"The first three items in the list are:\n{players[0:3]}")
print(f"Three items from the middle of the list are:\n{players[1:4]}")
print(f"The last three items in the list are:\n{players[-3:]}")
print("----------------------------------------------------------------------------------------")
#4.11
pizzas = ["pizzas_A","pizzas_B","pizzas_C"]
friend_pizzas=pizzas[:]
friend_pizzas.append("pizzas_D")
print("My favorite pizzas are:")
for i in pizzas:
    print(i)
print("My friend's favorite pizzas are:")
for i in friend_pizzas:
    print(i)
print("----------------------------------------------------------------------------------------")
#4.12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = ['pizza', 'falafel', 'carrot cake',"ice cream"]
for i in my_foods:
    print(i)
for i in friend_foods:
    print(i)
print("----------------------------------------------------------------------------------------")
#4.13
foods=("rice","noodle","pie","pizza","hamburger")
# foods[0]="beef"
foods=("beef","noodle","pork","pizza","hamburger")
