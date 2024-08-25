class GameStatus:
    def __init__(self,ai_game) -> None:
        self.settings = ai_game.settings
        self.high_score = 0                     #设置最高分
        self.reset_stats()
    
    def reset_stats(self):
        self.ships_left =self.settings.ship_limit
        self.score = 0