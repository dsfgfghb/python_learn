import pygame
from random import randint
from pygame.sprite import Sprite
from time import sleep
import sys

class Rain(Sprite):
    def __init__(self,window) -> None:
        super().__init__()
        self.screen = window.screen
        self.image = pygame.image.load("D:/vscode/python_learn/python_learn/alien_invasion/images/click_0.png")
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = randint(0,1600)
    def update(self):
        self.rect.y += 1
    def blime(self):
        self.screen.blit(self.image,self.rect)


class Window:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1600,800))
        self.clock = pygame.time.Clock()
        self.bg_color = (0,0,20)
        self.rains = pygame.sprite.Group()
        self.i=0
    def run(self):
        
        while True:
            self.screen.fill(self.bg_color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            if self.i == 0:
                rain = Rain(self)
                self.rains.add(rain)
            self.i+=1    
            self.i=self.i%5
            
            self.rains.update()
            self.rains.draw(self.screen)
            for rain in self.rains:
                if rain.rect.y > 800:
                    self.rains.remove(rain)
            pygame.display.flip()
            print(len(self.rains))
            self.clock.tick(60)

if __name__ == "__main__":
    window = Window()
    window.run()