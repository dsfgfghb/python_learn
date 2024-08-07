print("----------------------------------------------------------------------------------------")
#8.6.1 导入整个模块      
print("8.6.1 导入整个模块")

# import pizza          #假设有一个在该目录中名为pizza.py的文件

#pizza.py :
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")     
    for topping in toppings:
        print(f"- {topping}")

# pizza.make_pizza(16,'pepperoni')                                      #调用pizza内的函数
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')    

print("----------------------------------------------------------------------------------------")
#8.6.2 导入特定的函数   
print("8.6.2 导入特定的函数")
# from module_name import functong_name         可以只导入函数,从module_name里导入 functong_name
# from module_name import function_0, function_1, function_2    #用,隔开可以导入多个函数

# from pizza import make_pizza
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')          #导入函数后无需添加模块名

print("----------------------------------------------------------------------------------------")
#8.6.3使用as给函数指定别名   
print("8.6.3使用as给函数指定别名")

# from pizza import make_pizza as mp            #可以给导入的函数起一个别名

# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')  #直接用别名来调用函数

print("----------------------------------------------------------------------------------------")
#8.6.4使用as给模块指定别名   
print("8.6.4使用as给模块指定别名")
# import pizza as p                 #用as给pizza模块指定别名p

# p.make_pizza(16, 'pepperoni')                     #可以直接用别名,调用模块中的函数更轻松
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print("----------------------------------------------------------------------------------------")
#8.6.5 导入模块中的所有函数 
print("8.6.5 导入模块中的所有函数")

# from pizza import *           #*代表导入所有函数

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')      #导入所有函数后调用模块里的函数无需声明模块名

