import matplotlib.pyplot as plt

from random_walk import RandomWalk

# rw = RandomWalk()
# rw.fill_walk()

# fix , ax = plt.subplots()
# ax.scatter(rw.x_vlaue,rw.y_vlaue,s = 15)
# ax.set_aspect('equal')              #set_aspect() 指定两条轴上刻度的间距必须相等

# plt.show()

while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # fix , ax = plt.subplots()
    # fix , ax = plt.subplots(figsize = (15,9))       #调整输出尺寸   单位为英寸    Matplotlib假定屏幕的分辨率为每英寸 100 像素
    fix , ax = plt.subplots(figsize = (15,9),dpi=128)       

    point_numbers = range(rw.num_points)
    
    # ax.scatter(rw.x_vlaue,rw.y_vlaue,s = 15)

    ax.scatter(rw.x_vlaue,rw.y_vlaue,c=point_numbers,cmap=plt.cm.Blues,edgecolors = 'none',s = 1)      #edgecolor='none'删除所有点的轮廓
    
    ax.scatter(0,0,c="green",edgecolors='none',s=100)#突出起点
    ax.scatter(rw.x_vlaue[-1],rw.y_vlaue[-1],c='red',edgecolors='none',s=100)   #突出终点

    #隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)       

    ax.set_aspect('equal')              #set_aspect() 指定两条轴上刻度的间距必须相等

    plt.show()
    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break