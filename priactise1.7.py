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