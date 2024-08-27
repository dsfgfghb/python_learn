from random import choice

#创建游走类
class RandomWalk:
    def __init__(self,num_points = 5000):           #设置默认点数为5000
        self.num_points = num_points

        self.x_vlaue = [0]          #让所有游走都始于(0,0)
        self.y_vlaue = [0]

    def fill_walk(self):
        while len(self.x_vlaue) < self.num_points:
            x_direction = choice([1,-1])        #choice()随机选择列表中的一个值  这里选择方向
            x_distance = choice([0,1,2,3,4])        #选择行走的距离
            x_step = x_direction*x_distance
    
            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction*y_distance
    
            if x_step == 0 and y_step == 0:     #防止原地踏步
                continue

            x = self.x_vlaue[-1] + x_step       #计算下一个点的坐标值
            y = self.y_vlaue[-1] + y_step

            self.x_vlaue.append(x)
            self.y_vlaue.append(y)
            