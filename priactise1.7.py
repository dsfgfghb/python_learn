#6.1
person_inf = {
    'first_name' : 'Tom',
    'last_name' : 'sfd',
    'age' :18,
    'city' : 'beijing'    
}
for item in person_inf:
    print(person_inf.get(item))

print("----------------------------------------------------------------------------------------")
#6.2
favo_nom ={
    'A':0,
    'B':12,
    'C':123,
    'D':1234,
    'E':114514,
}
for item in favo_nom:
    print(favo_nom.get(item))
    
print("----------------------------------------------------------------------------------------")
#6.5
river= {
    'nile' : 'egypt',
    'changjiang' : 'china',
    'huanghe' : 'china'
}
for k,v in river.items():
    print(f"The {k} runs through {v}")
print("----------------------------------------------------------------------------------------")
#6.6
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python', 
}

namelist = {'jen','Tom','sarah','jerry'}
for i in namelist:
    if i in favorite_languages.keys():
        print(f"Thank you {i}")
    else:
        print(f"Could you join our Investigation? {i}.")

print("----------------------------------------------------------------------------------------")
#6.7
people_0 = {
    'name' : 'tom',
    'age' : 18,
}
people_1 = {
    'name' : 'jen',
    'age' : 27,
}
peoples = [people_0,people_1]

for people in peoples:
    print(f"Name :{people['name']}")
    print(f"Age: {people['age']}")
    
print("----------------------------------------------------------------------------------------")
#6.8
pet_0 = {
    'name' : 'Null',
    'species' : 'dog',
    'owner' :'tom',
}
pet_1 = {
    'name' : 'Undefined',
    'species' : 'cat',
    'owner' :'jen',
}
pets = [pet_0,pet_1]

for pet in pets:
    print(f"Name : {pet['name']}")
    print(f"Species : {pet['species']}")
    print(f"Owner : {pet['owner']}")
    
print("----------------------------------------------------------------------------------------")
#6.9
favorite_places = {
    'tom' : ['Beijing','Tianjing'],
    'jen' : ['USA','franch'],
    'sarah' : ["tom's house",'tom']
}
for person,places in favorite_places.items():
    print(f"Name : {person}")
    print("He/She like ")
    for place in places:
        print(place)

print("----------------------------------------------------------------------------------------")
#6.10
favo_nom ={
    'A':[0,1,2],
    'B':[10,12,14],
    'C':[123,234,345],
    'D':[1234],
    'E':[114514,999,1314],
}
for name,noms in favo_nom.items():
    print(f"{name} like")
    for nom in noms:
        print(nom)
