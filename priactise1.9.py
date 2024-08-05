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

print("----------------------------------------------------------------------------------------")
#8.6
def city_country(city,country):
    string =f"{city.lower().title()},{country.lower().title()}"
    return string
a = city_country('santiago','chile')
print(a)
a = city_country('guangzhou','China')
print(a)
a = city_country('Reykjavik',"Iceland")
print(a)

print("----------------------------------------------------------------------------------------")
#8.7
def make_album(name,album,nomber=None):
    singer = {'name':name,'album':album}
    if nomber:
        singer['nomber']=nomber
    return singer
singer = make_album('Anny','A big banana',1)
print(singer)

print("----------------------------------------------------------------------------------------")
#8.8
while True:
    print("Please tell me the singer name and album")
    print("(enter 'q' at any time to quit)")

    name=input('name:')
    if a=='q':
        break
    album = input('album:')
    if album =='q':
        break
    singer=make_album(name,album)
    print(singer)

print("----------------------------------------------------------------------------------------")
#8.9
words = ["hello" , 'hi' , 'goologe']
def show_messages(words):
    for word in words:
        print(word)
show_messages (words)

print("----------------------------------------------------------------------------------------")
#8.10
send_message = ["hello" , 'hi' , 'goologe']
sent_messages = []
def send_messages(send_message,sent_messages):
    while send_message:
        message = send_message.pop()
        print(message)
        sent_messages.append(message)

send_messages(send_message,sent_messages)
print(send_message)
print(sent_messages)

print("----------------------------------------------------------------------------------------")
#8.11

send_message = ["hello" , 'hi' , 'goologe']
sent_messages = []

send_messages(send_message[:],sent_messages[:])
print(send_message)
print(sent_messages)

print("----------------------------------------------------------------------------------------")
#8.12
def Description(*sandwich):
    for topping in sandwich:
        print(topping)

Description('mushrooms')
Description('mushrooms', 'green peppers')
Description('mushrooms', 'green peppers', 'extra cheese')

print("----------------------------------------------------------------------------------------")
#8.13

def build_profile(first_name,secend_name, **my_info):
    my_info['first_name'] = first_name
    my_info['second_name'] = secend_name
    return my_info
print (build_profile('feng' , 'jun' ,age=19))

print("----------------------------------------------------------------------------------------")
#8.14
def car_information(maker,type,**car_info):
    car_info['maker'] = maker
    car_info['type'] = type
    return car_info
print(car_information('subaru','outback',color='blue',tow_package=True))