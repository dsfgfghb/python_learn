magicians = ['alice', 'david', 'carolina']
for magician in magicians:                  #for循环遍历magicians里的元素,会反复将magicians里的元素赋给magician
    print(magician)                         #直到magicians里所有元素都被遍历完
    
for magician in magicians:                 
    print(magician.title() + ", that was a great trick!") 
    print(f"i can't wait to see your next trick,{magician.title()}.\n")
print("Thank you everyone, that was a great magic show!")
print("----------------------------------------------------------------------------------------")

for magician in magicians:      #  ":"不可以少会报错
#print(magician)             #后面的要循环的代码要缩进
    print(magician)
print(magician.title())           #该行代码没缩进,magician的值为最后一个元素的值

    #print(magician)            #一般情况下不能缩进
    
print("----------------------------------------------------------------------------------------")

for value in range(1,5):      # range(1,5)表示1到4的数字,左闭右开
    print(value)

nombers = list(range(1,6))    #可以用 list(range())生成一个列表
print(nombers)

nombers = list(range(2,11,2))       #range(2,11,2)表示从2开始,每次增加2,直到数字恰好不大于11 第一和第二个参数是范围,第三个参数是步长
print(nombers)

print("----------------------------------------------------------------------------------------")

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
