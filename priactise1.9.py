print("----------------------------------------------------------------------------------------")
#8.1
def display_message():
    print("The theme is functon")
display_message()

print("----------------------------------------------------------------------------------------")
#8.2
def favorites_book(title):
    print(f"One of my favorite books is {title}.")
favorites_book("Alice in Wonderland")

print("----------------------------------------------------------------------------------------")
#8.3

def make_shirt(size,word):
    print(f"Size:{size} \nword:{word}")
make_shirt('small','just do it')

print("----------------------------------------------------------------------------------------")
#8.4
def make_shirt(size,word='I love Python'):
    print(f"Size:{size} \nword:{word}")
make_shirt('big')
make_shirt('small','just do it')

print("----------------------------------------------------------------------------------------")
#8.5
def describe_city(name,nation='China'):
    print(f"{name.title()} is in {nation.title()}")
describe_city('guangzhou')
describe_city('shanhai')
describe_city('Reykjavik',"Iceland")
