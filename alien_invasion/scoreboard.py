import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    def __init__(self,ai_game) -> None:
        self.ai_game = ai_game          #
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.status

        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)        #字体大小以及字体类型

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        rounded_score = round(self.stats.score,-1)          #精确到小数点后一位
        # score_str = str(self.stats.score)
        score_str = f"{rounded_score:,}"            #:,是一个格式说明符,表示用逗号表示千分位分隔符  1,000

        

        self.score_image = self.font.render(score_str,True,self.text_color,self.settings.bg_color)      #设置背景颜色
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20          #设置位置为屏幕右端20位置处
        self.screen_rect.top = 20                           #设置顶端

    def prep_high_score(self):
        high_score = round(self.stats.high_score,-1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()

        self.high_score_rect.centerx = self.screen_rect.centerx         #放在顶部中央
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        if self.stats.score> self.stats.high_score:         #检查最高分
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str,True,self.text_color,self.settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):            #根据飞船数建立实体
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width        #设置x坐标
            ship.rect.y = 10
            self.ships.add(ship)
