import plotly.express as px
from die import Die


die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append (result)
# print(results)

frequencies = []                            #用来存储每个数字出现的次数
poss_results = range(1,die.num_sides+1)     
for value in poss_results:
    frequency = results.count(value)            #计算一个数字出现的个数
    frequencies.append(frequency)

title = "Results of Rolling One D5 1000 Times"      #设置title
labels = {'x':'Result','y':'Frequency of Result'}           #设置坐标轴的标签
# fig = px.bar(x=poss_results,y=frequencies)          #创建直方图
fig = px.bar(x=poss_results,y=frequencies,title=title,labels=labels)        #添加标签
fig.show()                                  #会将直方图渲染成HTML文件,并在浏览器打开
# print(frequencies)

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
poss_results = range(2,die_1.num_sides+die_2.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

fig = px.bar(x=poss_results,y=frequencies)
#进一步定制图形
fig.update_layout(xaxis_dtick=1)        #update_layout()传递了xaxis_dtick参数,该参数修改了x轴刻度的间距 若为1 x轴为1,2,3... 5 为 5,10,15...       

fig.show()

# 同时掷两个面数不同的骰子
die_2 = Die(10)
results = []
for roll_num in range(5_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
poss_results = range(2,die_1.num_sides+die_2.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
fig = px.bar(x=poss_results,y=frequencies)
fig.update_layout(xaxis_dtick=1)

fig.write_html('dice_visual_d6d10.html')            #以HTML的格式保存
fig.show()