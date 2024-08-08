print("----------------------------------------------------------------------------------------")
#9.1
class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type
    
    def describe_restaurant(self):
        print(f"Restaurant 's name is {self.restaurant_name}")
        print(f"Restaurant 's type is {self.cuisine_type}")
        
    def open_restaurant(self):
        print("The Restaurant is open")
    
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
        
    def describe_user(self):
        print(f"first name:{self.first_name} , last name: {self.last_name}")

    def greet_user(self):
        print(f"Hello! {self.first_name} {self.last_name}")

you = User('tom','sarar')
you.describe_user()
you.greet_user()