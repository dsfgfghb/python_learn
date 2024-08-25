import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_statue import GameStatus
from button import BUtton

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
        self.status = GameStatus(self)          #创建统计信息的实例
        self.ship = Ship(self)                  #创建飞船
        self.bullets = pygame.sprite.Group()        #子弹编组
        self.aliens = pygame.sprite.Group()         #外星人编组
        
        self._create_fleet()
        # self.game_active = True                 #游戏启动后处于活动状态
        self.game_active = False
        self.play_button = BUtton(self,"Play")
  
    def run_game(self):
        while True:     
            self._check_events()      

           
            # for event in pygame.event.get():        #侦听事件  pygame.event.get()用来访问监听到的事件
            #     if event.type==pygame.QUIT:         #检测玩家点击游戏窗口的关闭按钮
            #         sys.exit()              #退出游戏

            # self.screen.fill(self.settings.bg_color)    #用类设置屏幕
            # self.screen.fill(self.bg_color)         #每次循环都重绘屏幕  fill()接受一个颜色的实参,填充屏幕
            # self.ship.blime()
            if self.game_active:
                self.ship.update()          #每次循环都刷新一下飞船的位置
                self._update_bullets()
                self._update_aliens()
            # self.bullets.update()
            # for bullet in self.bullets.copy():      #进行for循环时必须保持列表长度不变,所以用copy
            #     if bullet.rect.bottom <= 0:         
            #         self.bullets.remove(bullet)         #删除子弹
            # print(len(self.bullets))

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
            elif event.type == pygame.MOUSEBUTTONDOWN:      #检测鼠标点击事件
                mouse_pos = pygame.mouse.get_pos()      #返回一个元祖包括点击鼠标是光标所在的x,y坐标
                self._check_play_button(mouse_pos)

                
            
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

        self.aliens.draw(self.screen)           #绘出alien



        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        if not self.game_active:
            self.play_button.draw_button()
        pygame.display.flip()
        
    
    def _update_bullets(self):
        self.bullets.update()
        # collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,False,True)     #检查是否碰撞
        #                 #如果rect重叠时,该函数在返回的字典中添加一个键值对 
        #                 #两个True表示去除对应的子弹和alien,若第一个为false 则只去除alien

        # if not self.aliens:             #检测alien是否为空
        #     self.bullets.empty()        #清空bullet
        #     self._create_fleet()
        self._check_bullet_alien_collisions()
        for bullet in self.bullets.copy():      
            if bullet.rect.bottom <= 0:         
                self.bullets.remove(bullet)         
            print(len(self.bullets))

    def _fire_bullet(self):                 #创建一个子弹,并将其加入编组
        if len(self.bullets)<self.settings.bullets_allowed:     #限制子弹数量
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _create_fleet(self):                #创建alien实例
        alien = Alien(self)     
        # alien_width = alien.rect.width    
        alien_width,alien_height = alien.rect.size  
        current_x,current_y=alien.rect.width,alien_height
        self.aliens.add(alien)
        while current_y<(self.settings.screen_height- 3 * alien_height):
            while current_x<(self.settings.screen_width - 2*alien_width):
                self._create_alien(current_x,current_y)
                # new_alien = Alien(self)
                # new_alien.x = current_x
                # new_alien.rect.x = current_x
                # self.aliens.add(new_alien)
                current_x+=alien_width
            current_x = alien_width
            current_y +=alien_height
    
    def _create_alien(self, x_position,y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position

        self.aliens.add(new_alien)
    
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):#spritecollideany() 函数接受两个实参：一个精灵和一个编组。
                                # 它检查编组是否有成员与精灵发生了碰撞，并在找到与精灵发生碰撞的成员后停止遍历编组aliens。
                                # 返回第一个与飞船发生碰撞的alien
            # print("Ship hit!")
            self._ship_hit()
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
       
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y +=self.settings.fleet_drop_speed
        self.settings.fleet_direction *=-1

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,False,True)     #检查是否碰撞
                        #如果rect重叠时,该函数在返回的字典中添加一个键值对 
                        #两个True表示去除对应的子弹和alien,若第一个为false 则只去除alien

        if not self.aliens:             #检测alien是否为空
            self.bullets.empty()        #清空bullet
            self._create_fleet()
            self.settings.increase_speed()

    def _ship_hit(self):
        if self.status.ships_left>0:    #判断是否还有飞船

            self.status.ships_left-=1

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()            #创建alien舰队
            self.ship.center_ship()         #将飞船放在屏幕中央底部

            sleep(0.5)          #暂停
        else:
            pygame.mouse.set_visible(True)
            self.game_active =False       #游戏标志
    
    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:    #判断是否到达底部
                self._ship_hit()
                break

    def _check_play_button(self,mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)  #判断鼠标点击所在位置是否为按钮的rect位置
        # if self.play_button.rect.collidepoint(mouse_pos):
        if button_clicked and not self.game_active:
            pygame.mouse.set_visible(False)             #设置光标不可见
            self.game_active = True
            self.status.reset_stats()

            self.bullets.empty()
            self.aliens.empty()

            self.settings.initialize_dynamic_settings()

            self._create_fleet()
            self.ship.center_ship()

if __name__ == '__main__':
    ai=AlienInvasion()
    ai.run_game()

