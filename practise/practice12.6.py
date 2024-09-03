import pygame
import sys
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,window) -> None:
        super().__init__()
        self.screen = window.screen
        self.settings = window.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.x = float(self.rect.x)
        self.x = window.rock.rect.x
        self.y = window.rock.rect.y
        self.rect.midbottom = (self.x,self.y)

    def update(self):
        self.x += self.settings.bullet_speed
    def draw_bullet(self):
        self.rect.x = self.x
        pygame.draw.rect(self.screen,self.color,self.rect)

class Settings:
    def __init__(self) -> None:
        self.screen_width = 1200
        self.screen_height = 800
        self.bullet_color = (0,0,60)
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed = 1.5

class Rock:
    def __init__(self,main_screen) -> None:
        self.screen = main_screen.screen    
        self.image = pygame.image.load("D:/vscode/javaScript/练习/image/Honkai  Star Rail Screenshot 2024.05.10 - 18.56.02.86.png")
        self.image= pygame.transform.scale(self.image,(256,160))
        self.rect = self.image.get_rect()
        # self.rock_moving_right = False
        # self.rock_moving_left = False
        self.rock_moving_up = False
        self.rock_moving_down = False

    def update(self):
        # if self.rock_moving_right and self.image_ract.right < self.screen.get_rect().right:
        #     self.image_ract.x += 1
        # if self.rock_moving_left and self.image_ract.left > 0:
        #     self.image_ract.x -= 1
        if self.rock_moving_up and self.image_ract.top > 0:
            self.image_ract.y -= 1
        if self.rock_moving_down and self.image_ract.bottom < self.screen.get_rect().bottom:
            self.image_ract.y += 1
    def blime(self):
        self.screen.blit(self.image,self.rect)

class Window:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1600,800))
        self.bg_color = (200,0,0)
        self.settings = Settings()
        self.rock = Rock(self)
        self.bullets = pygame.sprite.Group()
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.check_keydown_events(event)
                    print(event.key)
                if event.type == pygame.KEYUP:
                    self.check_keyup_events(event)
            self.screen.fill(self.bg_color)
            self.rock.update()

            self.bullets.update()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
                
            self.rock.blime()
            pygame.display.flip()
            
    def check_keydown_events(self,event):
        # if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        #     self.rock.rock_moving_right = True  
        # if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        #     self.rock.rock_moving_left = True
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.rock.rock_moving_up = True
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.rock.rock_moving_down = True
        if event.key == pygame.K_SPACE:
            self.bullets.add(Bullet(self))
    
    def check_keyup_events(self,event):
        # if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        #     self.rock.rock_moving_right = False
        # if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        #     self.rock.rock_moving_left = False
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.rock.rock_moving_up = False
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.rock.rock_moving_down = False

if __name__=='__main__':
    game = Window()
    game.run_game()