print("----------------------------------------------------------------------------------------")       
#11.1.1更新pip 
print("11.1.1更新pip")
#python -m pip install --upgrade pip        
#python -m pip是让Pythony运行pip模块
#install --upgrade pip  是让pip更新名为pip的第三方包

print("----------------------------------------------------------------------------------------")       
#11.1.2 安装 pytest 
print("11.1.2 安装 pytest")
# python -m pip install --user pytest

print("----------------------------------------------------------------------------------------")       
#11.2.3 可通过的测试 
print("11.2.3 可通过的测试")

def get_formatted_name(first, last):
    full_name = f"{first} {last}"
    return full_name.title()

def test_first_last_name():
    formatted_name = get_formatted_name('janis','joplin')
    assert formatted_name == 'Janis Joplin'                    #文件名必须以test_开头才能测试



print("----------------------------------------------------------------------------------------")       
#11.3 测试类 
print("11.3 测试类")

print("----------------------------------------------------------------------------------------")       
#11.3.4 使用夹具 
print("11.3.4 使用夹具")

