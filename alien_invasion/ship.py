import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_game) -> None:         #引入AlienInvasion 使ship可以访问AlienInvasion中定义的所有资源
        super().__init__()                      #继承sprite
        self.screen = ai_game.screen            #将屏幕赋给Ship 的一个属性 ,使这个类的方法可以轻松访问它
        self.setting = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()        #访问screen的rect属性 使飞船能后放到正确的位置

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('alien_invasion/images/OIP-C.jpg')  
        self.image = pygame.transform.smoothscale(self.image,(25,25))
        self.rect = self.image.get_rect()

    #如果要将游戏元素居中，可设置相应 rect 对象的属性 center、centerx 或 centery；
    #要让游戏元素与屏幕边缘对齐，可设置属性 top、bottom、left 或right。
    #除此之外，还有一些组合属性，如 midbottom、midtop、midleft 和 midright。
    #要调整游戏元素的水平或垂直位置，可使用属性 x 和 y，它们分别是相应矩形左上角的 x 坐标和 y 坐标。

        self.rect.midbottom = self.screen_rect.midbottom        # 每艘新飞船都放在屏幕底部的中央
        self.x = float(self.rect.x)                 #rect会将浮点数转化成整数,使用一个浮点数暂时存储位置,再赋给rect会更准确
        self.moving_right=False             #设置移动状态
        self.moving_left=False

    
    def blime(self):
        self.screen.blit(self.image,self.rect)          #绘制飞船
    def update(self):
        if self.moving_right and self.rect.x<self.screen_rect.right:
            self.x+=self.setting.ship_speed
        if self.moving_left and self.rect.x>self.screen_rect.left:
            self.x-=self.setting.ship_speed
        self.rect.x=self.x

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x  = float(self.rect.x)