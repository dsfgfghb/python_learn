import pygame
import sys

class Role:
    def __init__(self,window):
        self.screen = window.screen
        self.ract = pygame.Rect(0,0,50,50)
        self.image = pygame.image.load( "D:/vscode/javaScript/练习/image/1.jpg")
        # self.image = pygame.transform.smoothscale(self.image,(1000,50))
        self.image_ract = self.image.get_rect()
    def draw_role(self):
        self.screen.blit(self.image,self.ract)


class Window:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        self.bg_color = "Blue"
        self.role = Role(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.role.draw_role()
            pygame.display.flip()

if __name__ == '__main__':
    w = Window()
    w.run_game()