import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_game) -> None:
        super().__init__()   #继承sprite   #通过使用精灵（sprite），可将游戏中相关的元素编组，进而同时操作编组中的所有元素。
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height) #设置在0,0的矩形
        self.rect.midtop = ai_game.ship.rect.midtop #确定位置
        self.y = float(self.rect.y)     #将子弹位置化成float类型

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)