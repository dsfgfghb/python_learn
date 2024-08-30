from pathlib import Path
#csv文件格式
import csv
import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()       #splitlines()链式调用来获取一个包含文件各行的列表

reader = csv.reader(lines)                  #csv.reader() 函数 将包含 CSV 文件中各行的列表传递给reader
header_row = next(reader)                   #next() 返回文件中的下一行（从文件开头开始）
print(header_row)

for index,column_header in enumerate(header_row):#调用 enumerate() 来获取每个元素的索引及其值。
    print(index,column_header)

#读取数据
highs = []
for row in reader:
    high = int(row[4])              
    highs.append(high)
print(highs)

fig,ax= plt.subplots()
ax.plot(highs,color = 'red')            #将最高温传递给plot() 来绘制温度图

ax.set_title("Daily High Temperatures,Julyy 2021",fontsize = 24)
ax.set_xlabel('',fontsize = 16)
ax.set_ylabel('Temperature',fontsize = 16)
ax.tick_params(labelsize = 16)

plt.show()

from datetime import datetime 
first_date = datetime.strptime('2021-07-01','%Y-%m-%d') #strptime()将包含日期的字符串作为第一个实参。第二个实参告诉 Python 如何设置日期的格式。
                #'%Y-'表示让python家里那个字符串中第一个-字符串前面的部分视为年份
                # 参数 含义
                # %A 星期几，如 Monday
                # %B 月份名，如 January
                # %m 用数表示的月份（01～12）
                # %d 用数表示的月份中的一天（01～31）
                # %Y 四位数的年份，如 2019
                # %y 两位数的年份，如 19
                # %H 24 小时制的小时数（00～23）
                # %I 12 小时制的小时数（01～12）
                # %p am 或 pm
                # %M 分钟数（00～59）
                # %S 秒数（00～61）
print(first_date)

#在图中添加日期
dates,highs  = [],[]

path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)             
header_row = next(reader) 

for row in reader:
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)

fig,ax = plt.subplots()
ax.plot(dates,highs,color='red')
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)

fig.autofmt_xdate()                     #调用fig.autofmt_xdate() 来绘制 倾斜 的日期标签

ax.set_ylabel("Temperature(F)",fontsize = 16)
ax.tick_params(labelsize = 16)
plt.show()

#再绘制一个数据系列
dates,highs,lows  = [],[],[]

path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)             
header_row = next(reader) 

for row in reader:
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)        #

fig,ax = plt.subplots()
ax.plot(dates,highs,color='red',alpha = 0.5)
ax.plot(dates,lows,color = 'blue',alpha = 0.5)          #同时绘制两幅图     alpha代表透明度 1代表完全不透明

ax.fill_between(dates,highs,lows,facecolor ='blue',alpha = 0.1 )

ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)

fig.autofmt_xdate()                     #调用fig.autofmt_xdate() 来绘制 倾斜 的日期标签

ax.set_ylabel("Temperature(F)",fontsize = 16)
ax.tick_params(labelsize = 16)
plt.show()