#rstrip()   去除右端空白
#lstrip()   去除左端空白
#strip()   去除两端空白

favo_langage='Python    '

fa=f"{favo_langage},try"
print(fa)

favo_langage.rstrip()   #去除右段的空白

fa=f"{favo_langage},try"    #不会更改原内容，原变量仍然保持原样
print(fa)

favo_langage=favo_langage.rstrip()  #去除变量内右端的空格

fa=f"{favo_langage},try"
print(fa)

print("-----------------------------------------")


favo_langage="        python       "
print(f"{favo_langage.lstrip()}+sdf")
print(f"{favo_langage.strip()}+sdf")

nostarch_url='https://nostarch.com'
nostarch_url.removeprefix('https://') #去除前缀
print(nostarch_url.removeprefix('https://'))    

# message ='this's a message'  this 前后的'导致了python无法确定结束位置
message ="this 's a message"
print (message)
