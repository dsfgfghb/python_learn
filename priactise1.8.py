print("----------------------------------------------------------------------------------------")
#7.1
car = input("What kind of car you want?")
print(f"Let me see if I can find you a {car}")

print("----------------------------------------------------------------------------------------")
#7.2
nomber = input("How many people have meat?")
nomber = int(nomber)
if nomber > 8:
    print("There didn't have enough free table")
else:
    print("There have some free table")
    
print("----------------------------------------------------------------------------------------")
#7.2
nomber = input("Please tell me a nomber")
nomber = int(nomber)
if nomber % 10 == 0:
    print("Yes!")
else:
    print("No!")
