names=["tom","john","mary"]
for item in names:
    print(item)
for item in names:
    print(f"hello,{item}")
print("--------------------------------------------------------")

commute=['bus',"car","cycle"]
print(f"i would to go to school by {commute[-1]}")
print("--------------------------------------------------------")

for item in names:
    print(f"i would like to inviate {item} to my party")
    
print(f"{names[0]}can not come to my party")
names[0]="jane"
print(names)
print("--------------------------------------------------------")
for item in names:
    print(f"i would like to inviate {item} to my party")

names.append("jim")
names.insert(0,"bob")
names.insert(2,"alice")
print("--------------------------------------------------------")
for item in names:
    print(f"i would like to inviate {item} to my party")
print("--------------------------------------------------------")
nom=len(names)

for i in range(nom-1,-1,-1):
    if i>1:
        print(f"sorry,{names.pop()}, i can not invite you to my party")
    else:
        print(f"i would like to inviate {names[i]} to my party")