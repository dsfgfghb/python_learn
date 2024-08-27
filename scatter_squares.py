# 使用 scatter() 绘制散点图并设置样式
import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]

# plt.style.use('seabon')
fig,ax = plt.subplots()
# ax.scatter(1,4)                 #绘制单个点


# ax.scatter(2,4,s=2000)          #s 为点的大小
# ax.scatter(x_values,y_values,s = 100)       #绘制多个点

ax.set_title("Square Numbers",fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value",fontsize = 14)
ax.tick_params(labelsize =14)

#自动计算数据
x_values  = range(1,1001)
y_values = [x**2 for x in x_values]         #列表推导式 将每个x的平方赋给该列表
ax.scatter(x_values,y_values,s=20)

#定制刻度标记
ax.axis([0,1100,0,1_100_000])
ax.ticklabel_format(style='plain')

#定制颜色
# ax.scatter(x_values,y_values,color = 'red',s = 10)
# ax.scatter(x_values,y_values,color = (0,0.8,0),s=10)        #(红,绿,蓝) color 的值越靠近0,指点的颜色越浅

#使用颜色映射
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10)     #将y值较小的点为浅蓝色,较大的显示未深蓝色

#自动保存绘图
plt.savefig('squares_plot.png', bbox_inches='tight')        #在本目录保存
plt.savefig('D:/picture/Screenshots/squares_plot.png', bbox_inches='tight')        #指定路径保存

plt.show()

