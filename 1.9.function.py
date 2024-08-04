print("----------------------------------------------------------------------------------------")
#8.1.1向函数传递信息
print("8.1.1向函数传递信息")
def greet_user():               
    print("Hello!")

greet_user()

def greet_user(username):                   #直接写参数名,可以传递参数
    print(f"Hello {username.title()}!")

greet_user('jesse')
print("----------------------------------------------------------------------------------------")
#8.1.2 实参和形参
print("8.1.2 实参和形参")
def greet_user(username):                   # username为形参 ,'Jesse'为实参
    print(f"Hello {username.title()}!")

greet_user('jesse')

print("----------------------------------------------------------------------------------------")
#8.2.1 位置实参
print("8.2.1 位置实参")
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')           #多次调用函数

print("----------------------------------------------------------------------------------------")
#8.2.1 位置实参的顺序
print("8.2.1 位置实参的顺序")
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('harry', 'hamster')                    #要注意参数的顺序

print("----------------------------------------------------------------------------------------")
#8.2.2关键字实参
print("8.2.2关键字实参")

def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type="hamster",pet_name="harry")            #可以用关键字实参来赋值,无需考虑实参顺序
describe_pet(pet_name="harry",animal_type="hamster")  

print("----------------------------------------------------------------------------------------")
#8.2.3默认值
print("8.2.3默认值")

def describe_pet(pet_name,animal_type = 'dog'):               #(形参=默认值)可以给函数赋一个默认值
    print(f"\nI have a {animal_type}.")                         #设置默认值时必须将所有没有默认值的形参写在前面,否则会报错
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('willie')

print("----------------------------------------------------------------------------------------")
#8.2.4等效的函数调用
print("8.2.4等效的函数调用")

def describe_pet(pet_name,animal_type = 'dog'):               
    print(f"\nI have a {animal_type}.")                        
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie')
describe_pet(pet_name='willie')             

describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')       #函数的多种调用方式

print("----------------------------------------------------------------------------------------")
#8.2.5 避免实参错误
print("8.2.5 避免实参错误")
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet()                              #会报错,实参数量不对

print("----------------------------------------------------------------------------------------")
#8.3.1返回简单的值
print("8.3.1返回简单的值")
def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name                            #返回一个变量
musician = get_formatted_name('jimi','hendrix')
print(musician)

print("----------------------------------------------------------------------------------------")
#8.3.2 让实参变成可选的
print("8.3.2 让实参变成可选的")
def get_formatted_name(first_name, last_name, middle_name=''):          #给middle_name一个默认值使实参变得可选
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
musician = get_formatted_name('john', 'hooker')
print(musician)

print("----------------------------------------------------------------------------------------")
#8.3.3 返回字典
print("8.3.3 返回字典")
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person                                           #可以直接返回一个字典
musician = build_person('jimi', 'hendrix')
print(musician)
def build_person(first_name, last_name,age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age']= age
    return person                                      
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

print("----------------------------------------------------------------------------------------")
#8.3.4 结合使用函数和 while 循环
print("8.3.4 结合使用函数和 while 循环")
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")

    if f_name == 'q':
        break

    l_name = input("Last name: ")

    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)         #在while循环中调用函数
    print(f"\nHello, {formatted_name}!")
    
