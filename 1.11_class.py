print("----------------------------------------------------------------------------------------")
#9.1.1创建Dog类 
print("9.1.1创建Dog类")

class Dog:                          #根据约定，在 Python 中，首字母大写的名称指的是类。
    def __init__(self,name,age):    #类中的函数被称为方法.
        self.name = name            #__init__是一个特殊方法,每次创造该类的新实例后都会自动运行
                                    #self必不可少,self会自动传递,创建实例时无需提供self
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        print(f"{self.name} rolled over!")

print("----------------------------------------------------------------------------------------")
#9.1.2 根据类创建实例 
print("9.1.2 根据类创建实例")

my_Dog = Dog('willie',6)
print(f"My dog's name is {my_Dog.name}.")           #访问属性时可以使用 . 
print(f"My dog is {my_Dog.age} years old.")
my_Dog.sit()                                #用.调用方法
my_Dog.roll_over()  

your_dog = Dog('Lucy',3)
print(f"your dog's name is {your_dog.name}.")           #创建多个类
print(f"your dog is {your_dog.age} years old.")
your_dog.sit()