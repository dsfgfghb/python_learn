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