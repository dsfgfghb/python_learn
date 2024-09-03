import pygame
from random import randint
from pygame.sprite import Sprite
import sys

class Star(Sprite):
    def __init__(self,window) -> None:
        super().__init__()
        self.screen = window.screen
        self.image = pygame.image.load("D:/vscode/python_learn/python_learn/alien_invasion/images/OIP-C.jpg")
        self.image= pygame.transform.scale(self.image,(10,10))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0,1600)
        self.rect.y = randint(0,800)
    def blime(self):
        self.screen.blit(self.image,self.rect)

class Window:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1600,800))
        self.bg_color = (0,0,20)
        self.stars = pygame.sprite.Group()
        for i in range(100):
            self.stars.add(Star(self))
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  
            self.screen.fill(self.bg_color)
            self.stars.draw(self.screen)
            pygame.display.flip()

if __name__ == "__main__":
    window = Window()
    window.run()
