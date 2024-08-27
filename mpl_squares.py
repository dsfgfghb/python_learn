import matplotlib.pyplot as plt

plt.style.available     #设定样式
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]     
# plt.style.use('seaborn')      #设定样式
fig,ax = plt.subplots() #这个函数可在一个图形（figure）中绘制一或多个绘图（plot）;变量 fig 表示由生成的一系列绘图构成的整个图形。变量 ax 表示图形中的绘图

# ax.plot(squares)        #绘制绘图
# ax.plot(squares,linewidth = 3)      #修改绘制的线条的粗细为3   plot() 提供一个数值序列时，它假设第一个数据点对应的x坐标值为 0,所以这样画出的图不准确
ax.plot(input_values,squares,linewidth = 3)      #同时提供输入值和输出值

#设置图题
ax.set_title("Squarre Numbers",fontsize = 24)
#给x,y坐标轴加上标签
ax.set_xlabel("Value",fontsize = 24)
ax.set_ylabel("Square of Value",fontsize = 14)

ax.tick_params(labelsize = 14)      #tick_params()用来设置刻度的样式  这里是把刻度标记的字号设置为14

plt.show()          #打开Matplotlib查看器并形式绘图


