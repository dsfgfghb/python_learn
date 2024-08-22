import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game) -> None:
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('alien_invasion/images/alien.png')
        self.image = pygame.transform.smoothscale(self.image,(100,100))
        self.rect =self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)