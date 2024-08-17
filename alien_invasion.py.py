import sys
import pygame
from settings import Settings

class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()                               #初始化背景

        self.clock = pygame.time.Clock()            #创建时钟
        self.settings = Settings()                       #用类来设置初始值
        # self.bg_color = (230, 230, 230)             #设置颜色
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height) )   #

        # self.screen =  pygame.display.set_mode((1200,800))  #创建一个显示窗口  (1200,800)为窗口尺寸
        pygame.display.set_caption("Alien Invasion")    

    def run_game(self):
        while True:                                 
            for event in pygame.event.get():        #侦听事件  pygame.event.get()用来访问监听到的事件
                if event.type==pygame.QUIT:         #检测玩家点击游戏窗口的关闭按钮
                    sys.exit()              #退出游戏

            self.screen.fill(self.settings.bg_color)    #用类设置屏幕

            # self.screen.fill(self.bg_color)         #每次循环都重绘屏幕  fill()接受一个颜色的实参,填充屏幕
            self.clock.tick(60)             #开始计时   ()内为帧率   Pygame 将尽可能确保这个循环每秒恰好运行 60 次。

            pygame.display.flip()           #显示屏幕

if __name__ == '__main__':
    ai=AlienInvasion()
    ai.run_game()

