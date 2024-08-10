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

print("----------------------------------------------------------------------------------------")
#9.2.1使用类和实例 
print("9.2.1使用类和实例")

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

print("----------------------------------------------------------------------------------------")
#9.2.2给属性指定默认值 
print("9.2.2给属性指定默认值")
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

print("----------------------------------------------------------------------------------------")
#9.2.3 修改属性的值 
print("9.2.3 修改属性的值")

my_new_car.odometer_reading = 23            #直接通过实例访问
my_new_car.read_odometer()

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):                              #通过方法修改
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):                         #通过方法令该值递增
        self.odometer_reading+=miles
    
my_new_car = Car('audi', 'a4', 2024)
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car=Car('subaru','outback',2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

print("----------------------------------------------------------------------------------------")
#9.3.1继承 子类的__init__()方法 
print("9.3.1继承 子类的__init__()方法")

class ElectricCar(Car):                 #()内为父类名称
    def __init__(self, make, model, year):          
        super().__init__(make, model, year)          #super()能够调用父类的__init__()方法 父类也被称为超类

my_leaf = ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
    
print("----------------------------------------------------------------------------------------")
#9.3.2 给子类定义属性和方法 
print("9.3.2 给子类定义属性和方法")

class ElectricCar(Car):                 
    def __init__(self, make, model, year):          
        super().__init__(make, model, year) 
        self.battery_size = 40
    
    def describe_battary(self):
        print(f"This car has a {self.battery_size}-kwh battary.")

my_leaf = ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battary()

print("----------------------------------------------------------------------------------------")
#9.3.3 重写父类中的方法 
print("9.3.3 重写父类中的方法")
class ElectricCar(Car):                 
    def __init__(self, make, model, year):          
        super().__init__(make, model, year) 
        self.battery_size = 40
    
    def describe_battary(self):
        print(f"This car has a {self.battery_size}-kwh battary.")

    def fill_gas_tank(self):                                #假设父类Car内有该函数,若在子类调用该函数,python会
                                                            #忽略父类的函数,执行子类的该函数
        print("This car doesn't have a gas tank!")          

print("----------------------------------------------------------------------------------------")
#9.3.4 将实例用作属性 
print("9.3.4 将实例用作属性")
class Battery:
    def __init__(self,battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")
    
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battary = Battery()                #可以给属性赋一个实例

my_leaf = ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
my_leaf.battary.describe_battery()
my_leaf.battary.get_range()
