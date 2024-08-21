import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()                               #初始化背景

        self.clock = pygame.time.Clock()            #创建时钟
        self.settings = Settings()                       #用类来设置初始值
        
        # self.bg_color = (230, 230, 230)             #设置颜色
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)      #全屏
        # self.settings.screen_width= self.screen.get_rect().width
        # self.settings.screen_height= self.screen.get_rect().height
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height) )   #

        # self.screen =  pygame.display.set_mode((1200,800))  #创建一个显示窗口  (1200,800)为窗口尺寸
        pygame.display.set_caption("Alien Invasion")    
        self.ship = Ship(self)                  #创建飞船
        self.bullets = pygame.sprite.Group()        #子弹编组
  
    def run_game(self):
        while True:     
            self._check_events()             
            # for event in pygame.event.get():        #侦听事件  pygame.event.get()用来访问监听到的事件
            #     if event.type==pygame.QUIT:         #检测玩家点击游戏窗口的关闭按钮
            #         sys.exit()              #退出游戏

            # self.screen.fill(self.settings.bg_color)    #用类设置屏幕
            # self.screen.fill(self.bg_color)         #每次循环都重绘屏幕  fill()接受一个颜色的实参,填充屏幕
            # self.ship.blime()
            self.ship.update()          #每次循环都刷新一下飞船的位置
            self.bullets.update()
            self._update_screen()
            self.clock.tick(60)             #开始计时   ()内为帧率   Pygame 将尽可能确保这个循环每秒恰好运行 60 次。

            # pygame.display.flip()           #显示屏幕
            
    # def _check_events(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             sys.exit()
    #         elif event.type==pygame.KEYDOWN:
    #             if event.key == pygame.K_RIGHT:     #检查按下的将是否为右方向键
    #                 # self.ship.rect.x +=20
    #                 self.ship.moving_right=True
    #             elif event.key == pygame.K_LEFT:
    #                 self.ship.moving_left=True
    #         elif event.type==pygame.KEYUP:
    #             if event.key == pygame.K_RIGHT:
    #                 self.ship.moving_right = False
    #             elif event.key == pygame.K_LEFT:
    #                 self.ship.moving_left = False

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
            
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:     
            self.ship.moving_right=True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left=True
        elif event.key == pygame.K_q :
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            # sys.exit()
            
        
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:     
            self.ship.moving_right=False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left=False
               

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color) 
        self.ship.blime()
        pygame.display.flip()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
    
    def _fire_bullet(self):                 #创建一个子弹,并将其加入编组
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

if __name__ == '__main__':
    ai=AlienInvasion()
    ai.run_game()

