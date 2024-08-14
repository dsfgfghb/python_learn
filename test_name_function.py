def get_formatted_name(first, last):
    full_name = f"{first} {last}"
    return full_name.title()

def get_formatted_name(first, middle, last):
    full_name = f"{first} {middle} {last}"
    return full_name.title()

def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

def test_first_last_name():                         #函数名必须test开头
    formatted_name = get_formatted_name('janis','joplin')           #终端输入pytest开始测试
    assert formatted_name == 'Janis Joplin'                           #断言  声称该变量的字为"Janis Joplin'

def test_first_last_middle_name():
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'

