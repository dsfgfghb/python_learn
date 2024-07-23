import re
person1="Eric"
print(f"Hello {person1},would you like to learn some Python today?")

person2="tom"
print(person2.lower())
print(person2.upper())
print(person2.title())

print('Albert Einstein once said,"A person who never made a mistake never tried anything new"')

person3="   jerry \t \n   "
print(person3.lstrip(' '))
print(person3.rstrip(' '))
print(person3.strip(' '))

the_url='https://nostarch.com'
print(the_url.removeprefix('https://'))
print(the_url.removesuffix('.com'))
print(the_url.removeprefix('https://').removesuffix('.com'))

# string="sdfnj129032313kd78907fsj890k"
# print(re.findall('[0-9]+',string)[2])

# class s:
#     def __init__(self,n) -> None:
#         self.name=n
#         self.next=None
#     def show(self):
#         print(self.name)

# a=s("sd")

# a.next=s("nddf")
# a.show()
# a.next.show()