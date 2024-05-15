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