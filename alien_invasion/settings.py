class Settings:
    def __init__(self) -> None:
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed = 5

        self.bullet_speed = 100
        self.bullet_width = 200
        self.bullet_height = 5
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 10

        self.alien_speed = 3.0
        self.fleet_drop_speed = 5
        self.fleet_direction = 1