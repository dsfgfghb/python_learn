print("----------------------------------------------------------------------------------------")
#9.1
class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"Restaurant 's name is {self.restaurant_name}")
        print(f"Restaurant 's type is {self.cuisine_type}")
        
    def open_restaurant(self):
        print("The Restaurant is open")
    
    def set_number_served(self,number):
        self.number_served=number
    
    def  increment_number_served(self,number):
        self.number_served+=number

        
    
a=Restaurant('sfoods','big')
print(f'name: {a.restaurant_name} cuisine_type: {a.cuisine_type}')
a.describe_restaurant()
a.open_restaurant()

print("----------------------------------------------------------------------------------------")
#9.2
a=Restaurant('sfoods','big')
b=Restaurant('afoods','mid')
c=Restaurant('cfoods','small')
a.describe_restaurant()
b.describe_restaurant()
c.describe_restaurant()

print("----------------------------------------------------------------------------------------")
#9.3

class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"first name:{self.first_name} , last name: {self.last_name}")

    def greet_user(self):
        print(f"Hello! {self.first_name} {self.last_name}")
    
    def increment_login_attempts(self):
        self.login_attempts+=1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


you = User('tom','sarar')
you.describe_user()
you.greet_user()

print("----------------------------------------------------------------------------------------")
#9.4
restaurant = Restaurant('Abc','big')
restaurant.number_served = 10
print(restaurant.number_served)

restaurant.set_number_served(222)
print(restaurant.number_served)

restaurant.increment_number_served(30)
print(restaurant.number_served)

print("----------------------------------------------------------------------------------------")
#9.5
Tom = User('Tom','sarae')
print(Tom.login_attempts)
for i in range(10):
    Tom.increment_login_attempts()
print(Tom.login_attempts)
Tom.reset_login_attempts()
print(Tom.login_attempts)


print("----------------------------------------------------------------------------------------")
#9.6
class IceCreamStand(Restaurant):
    def __init__(self, name, type,flavors):
        super().__init__(name, type)
        self.flavors=flavors
    
    def show_flavor(self):
        print("I like :")
        for item in self.flavors:
            print(item)
    
ice= IceCreamStand('hh','big',['1','8'])
ice.show_flavor()


print("----------------------------------------------------------------------------------------")
#9.7
class Admin(User):
    def __init__(self, first_name, last_name,privileges):
        super().__init__(first_name, last_name)
        self.privileges=privileges
    
    def show_privileges(self):
        print("your privileges:")
        for privilege in self.privileges:
            print(privilege)

anna=Admin("anna",'taff',["can add post","can deletepost","can ban user"])
anna.show_privileges()

print("----------------------------------------------------------------------------------------")
#9.8
class Pribileges:
    def __init__(self,privileges):
        self.privileges=privileges
    
    def show_privileges(self):
        print("Your privileges:")
        for item in self.privileges:
            print(item)

a=Admin('a','b',Pribileges(["can add post","can deletepost","can ban user"]))
a.privileges.show_privileges()
